from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

class FeatureSelector:
    def __init__(self):
        self.selected_features = None
        
    def select_features_univariate(self, X, y, k=5):
        """Select top k features using univariate selection"""
        selector = SelectKBest(score_func=f_regression, k=k)
        X_selected = selector.fit_transform(X, y)
        selected_features = X.columns[selector.get_support()].tolist()
        
        self.selected_features = selected_features
        return X[selected_features]
    
    def select_features_rfe(self, X, y, n_features=5):
        """Select features using Recursive Feature Elimination"""
        estimator = LinearRegression()
        selector = RFE(estimator, n_features_to_select=n_features)
        selector.fit(X, y)
        
        selected_features = X.columns[selector.support_].tolist()
        self.selected_features = selected_features
        return X[selected_features]
