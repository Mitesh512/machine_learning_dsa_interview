from fastapi import FastAPI, Request, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import asyncio
import redis
import hashlib
import logging
from typing import Optional

app = FastAPI(title="Advanced API Gateway")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api-gateway")

redis_client = redis.Redis(host='localhost', port=6379, db=0)

security = HTTPBearer()
API_KEY = "my-secret-api-key"
RATE_LIMIT = 5
RATE_LIMIT_WINDOW = 60

# Rate limiter
def rate_limiter(ip: str):
    key = f"rate:{ip}"
    current = redis_client.get(key)
    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    pipe = redis_client.pipeline()
    pipe.incr(key, 1)
    pipe.expire(key, RATE_LIMIT_WINDOW)
    pipe.execute()

# Cache helpers
def get_cache_key(path: str):
    return "cache:" + hashlib.sha256(path.encode()).hexdigest()

async def get_cached_response(path: str):
    key = get_cache_key(path)
    cached = redis_client.get(key)
    if cached:
        return JSONResponse(content=eval(cached.decode()))
    return None

async def set_cached_response(path: str, response_data):
    key = get_cache_key(path)
    redis_client.setex(key, 30, str(response_data))

# JWT (mocked)
def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != "valid-jwt-token":
        raise HTTPException(status_code=401, detail="Invalid or missing JWT token")

# API Key check
def check_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

# Log requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    return await call_next(request)

@app.get("/login", dependencies=[Depends(verify_jwt), Depends(check_api_key)])
async def route_login(request: Request):
    rate_limiter(request.client.host)
    if cached := await get_cached_response("/login"):
        return cached
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://localhost:8001/login")
        await set_cached_response("/login", resp.json())
        return resp.json()

@app.get("/orders", dependencies=[Depends(verify_jwt), Depends(check_api_key)])
async def route_orders(request: Request):
    rate_limiter(request.client.host)
    if cached := await get_cached_response("/orders"):
        return cached
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://localhost:8002/orders")
        await set_cached_response("/orders", resp.json())
        return resp.json()

@app.get("/products", dependencies=[Depends(verify_jwt), Depends(check_api_key)])
async def route_products(request: Request):
    rate_limiter(request.client.host)
    if cached := await get_cached_response("/products"):
        return cached
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://localhost:8003/products")
        await set_cached_response("/products", resp.json())
        return resp.json()

@app.get("/dashboard", dependencies=[Depends(verify_jwt), Depends(check_api_key)])
async def aggregated_response(request: Request):
    rate_limiter(request.client.host)
    async with httpx.AsyncClient() as client:
        auth_task = client.get("http://localhost:8001/login")
        orders_task = client.get("http://localhost:8002/orders")
        products_task = client.get("http://localhost:8003/products")
        auth_res, orders_res, products_res = await asyncio.gather(auth_task, orders_task, products_task)
        return {
            "auth": auth_res.json(),
            "orders": orders_res.json(),
            "products": products_res.json()
        }
