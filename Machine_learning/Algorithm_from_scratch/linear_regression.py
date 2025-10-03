import numpy as np


# --------------------------------
# Data handler Class
# --------------------------------

class DataHandler:
    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.normalize()
        
    def normalize(self):
        self.X = (self.X - np.mean(self.X, axis = 0)) / (np.std(self.X, axis=0))

    def train_test_split(self,test_size = 0.2, seed = 0):
        np.random.seed(seed)
    
        indices = np.arange(self.X.shape[0])
        np.random.shuffle(indices)
        
        split_idx = int(self.X.shape[0] * (1-test_size))
        train_idx, test_idx = indices[:split_idx], indices[split_idx:]
        
        return (self.X[train_idx], self.X[test_idx], self.y[train_idx], self.y[test_idx])
    
    
# --------------------------------
# Linear Regression Class
# --------------------------------


class LinearRegression:
    def __init__(self, lr = 0.01, epochs= 100):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
    
    def fit(self,X,y):
        n_samples, n_features = X.shape[0], X.shape[1]
        self.weights = np.random.randn(n_features,1)
        self.bias = np.random.randn(1)
        
        for _ in range(self.epochs):
            # pred
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Grads
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # updated params
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    
    def predict(self, X):
        return np.dot(X, self.weights)  + self.bias

# --------------------------------
# Regression Metrics
# --------------------------------


class RegressionMetrics:
    def __init__(self,y_true, y_pred):
        self.y_true = y_true.reshape(-1,1)
        self.y_pred = y_pred.reshape(-1,1)
    
    
    def mse(self):
        return np.mean((self.y_true - self.y_pred) ** 2)

    def mae(self):
        return np.mean(np.abs(self.y_true - self.y_pred))
    
    def r2_score(self):
        ss_res = np.sum((self.y_true - self.y_pred)**2)
        ss_total = np.sum((self.y_true - np.mean(self.y_true, axis=0))**2)
        if ss_total == 0:
            return 0
        return 1 - (ss_res/ss_total)
    
    def all_metrics(self):
        return {
            "MSE": round(self.mse(),4), 
            "MAE": round(self.mae(), 4),
            "R2_Score": round(self.r2_score(), 4)
        }



if __name__ == "__main__":
    np.random.seed(2)
    num_samples = 500
    num_features = 5
    
    X = np.random.rand(num_samples, num_features)
    true_weights = np.random.randn(num_features,1)
    y = X @ true_weights + np.random.randn(num_samples ,1 )
    
    # data preparation
    data = DataHandler(X,y)
    X_train, X_test , y_train, y_test = data.train_test_split(test_size=0.2, seed=0)
    
    # training
    model = LinearRegression(lr=0.05, epochs=50)
    model.fit(X_train, y_train)
    
    # predict
    preds = model.predict(X_test)
    
    # metrices
    metrics = RegressionMetrics(y_test, preds)
    print(metrics.all_metrics())
    
        
        








