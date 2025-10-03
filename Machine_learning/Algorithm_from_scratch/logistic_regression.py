import numpy as np


# ----------------------------------------
# Data Handler Class
# ----------------------------------------

class DataHandler:
    def __init__(self,X,y):
        self.X = X
        self.y = y.reshape(-1,1)
        self.normalize()
    def normalize(self):
        self.X = (self.X - np.mean(self.X,axis=0)) / np.std(self.X,axis= 0)
    
    def train_test_split(self,test_size, seed):
        np.random.seed(seed)
        
        indices = np.arange(self.X.shape[0])
        np.random.shuffle(indices)
        
        split_idx = int(self.X.shape[0] * (1-test_size))
        train_idx, test_idx = indices[:split_idx] , indices[split_idx:]
        
        return (self.X[train_idx], self.X[test_idx], 
                self.y[train_idx], self.y[test_idx])



# ----------------------------------------
# Logistic Regression Class 
# ----------------------------------------

class LogisticRegression:
    def __init__(self,lr= 0.01, epochs= 100):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
    
    def sigmoid(self, z):
        return (1/ (1 + np.exp(-z)))
    
    def fit(self,X, y):
        n_samples, n_features = X.shape
        self.weights = np.random.rand(n_features, 1)
        self.bias = 0
        
        for i in range(self.epochs):
            # linear model
            z = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(z)
            
            # compute gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # update parameters 
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            

    def predict(self,X):
        z = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(z)
        
        return (y_pred > 0.5).astype(int)


# ----------------------------------------
# Metrics Calculation Class
# ----------------------------------------

class Metrices:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
        self.TP = None
        self.FP= None
        self.TN = None 
        self.FN = None
        
        self._compute_confusion_matrix()
    
    
    def _compute_confusion_matrix(self):
        self.TP = np.sum((self.y_true == 1) & (self.y_pred == 1))
        self.FP = np.sum((self.y_true == 0) & (self.y_pred == 1))
        self.TN = np.sum((self.y_true == 0) & (self.y_pred == 0))
        self.FN = np.sum((self.y_true == 1) & (self.y_pred == 0))
    
    def accuracy(self):
        total_accurate = self.TP + self.TN
        total = self.TP + self.FP + self.TN + self.FN 
        if total == 0:
            return 0
        else:
            return round(total_accurate/ total,4)
    
    def precision(self):
        # TP / TP + FP
        denmr = self.TP + self.FP 
        if denmr == 0:
            return 0
        return round(self.TP / denmr,4)

    def recall(self):
        # TP / TP + FN
        den = self.TP + self.FN
        if den == 0:
            return 0 
        return round(self.TP / den,4)
    
    def f1_score(self):
        prec = self.precision()
        rec = self.recall()
        if prec + rec == 0:
            return 0
        
        return round((2* prec * rec) / (prec + rec),4)

    def all_metrices(self):
        return {
            "accuracy": self.accuracy(),
            "precision": self.precision(),
            "recall": self.recall(),
            "f1_score":self.f1_score()
            }
    

if __name__ == "__main__":

    np.random.seed(512)
    num_samples = 500
    num_features = 5
    X = np.random.rand(num_samples, num_features)
    # y = np.random.randint(0, 2, 500)
    y_continuous = 3 * X.squeeze() + 4 + np.random.randn(num_samples,num_features) * 0.3
    y = (y_continuous > y_continuous.mean()).astype(int)
    
    data = DataHandler(X, y)
    X_train, X_test, y_train, y_test = data.train_test_split(test_size=0.15, seed=0)
    
    model = LogisticRegression(lr = 0.01, epochs=100)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)

    
    metrices = Metrices(y_test, preds)
    print(metrices.all_metrices())
