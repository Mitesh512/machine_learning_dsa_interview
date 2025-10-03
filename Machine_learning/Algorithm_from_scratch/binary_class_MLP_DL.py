import numpy as np

## Activation Funcitons
def relu(x):
    return np.maximum(0,x)

def relu_derivative(x):
    return np.where(x>0,1,0)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1-s)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis= 1, keepdims = True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

def softmax_derivative(x):
    return 1

def linear(x):
    return x 

def linear_derivative(x):
    return 1
    

#### defininf loss functions
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def mse_derivative(y_true, y_pred):
    return 2 * (y_true - y_pred) * (1/ y_true.shape[0])

def binary_cross_entropy_loss(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-9, 1- 1e-9) # to avoid log(0)
    # (1/n) *  sum{ -ylog(y^) - (1-y)log(1-y^)}
    return np.mean(y_true * np.log(y_pred) + (1-y_true) * np.log(1-y_pred))

def bce_derivative(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-9 , 1-1e9)
    return (y_pred - y_true) / ( y_pred * (1 - y_pred)* y_true.shape[0])
    


    




