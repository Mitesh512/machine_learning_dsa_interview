import mlflow
import optuna
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import numpy as np

class ModelTrainer:
    def __init__(self, random_state=42):
        self.random_state = random_state
        
    def train_model(self, X_train, y_train, params):
        """Train the model with given parameters"""
        model = ElasticNet(random_state=self.random_state, **params)
        model.fit(X_train, y_train)
        return model
    
    def evaluate_model(self, model, X_test, y_test):
        """Evaluate the model performance"""
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        return {
            'rmse': rmse,
            'r2': r2
        }
    
    def objective(self, trial, X_train, y_train):
        """Objective function for hyperparameter optimization"""
        params = {
            'alpha': trial.suggest_loguniform('alpha', 1e-4, 1.0),
            'l1_ratio': trial.suggest_uniform('l1_ratio', 0.1, 0.9),
            'max_iter': trial.suggest_int('max_iter', 100, 300)
        }
        
        model = self.train_model(X_train, y_train, params)
        scores = cross_val_score(
            model, X_train, y_train, 
            cv=5, scoring='neg_mean_squared_error'
        )
        rmse = np.sqrt(-scores.mean())
        
        return rmse
    
    def optimize_hyperparameters(self, X_train, X_test, y_train, y_test n_trials=100):
        """Optimize hyperparameters using Optuna"""
        study = optuna.create_study(direction='minimize')
        study.optimize(
            lambda trial: self.objective(trial, X_train, y_train),
            n_trials=n_trials
        )
        
        return study.best_params
