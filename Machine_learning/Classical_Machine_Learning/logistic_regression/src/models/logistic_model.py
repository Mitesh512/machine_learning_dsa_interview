"""
Logistic Regression Model Implementation

This module provides a class for training and using logistic regression models
with scikit-learn, including methods for evaluation and interpretation.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


class LogisticClassifier:
    """
    A wrapper class for scikit-learn's LogisticRegression with additional functionality
    for model evaluation and interpretation.
    """
    def __init__(self, penalty='l2', C=1.0, multi_class='auto', random_state=42, **kwargs):
        """
        Initialize the logistic regression classifier.
        
        Args:
            penalty (str): Type of regularization ('l1', 'l2', 'elasticnet', 'none')
            C (float): Inverse of regularization strength
            multi_class (str): Strategy for multi-class ('auto', 'ovr', 'multinomial')
            random_state (int): Random state for reproducibility
            **kwargs: Additional arguments for sklearn.linear_model.LogisticRegression
        """
        self.model = LogisticRegression(
            penalty=penalty,
            C=C,
            multi_class=multi_class,
            random_state=random_state,
            **kwargs
        )
        self.feature_names = None
        self.is_fitted = False
    
    def fit(self, X, y, feature_names=None):
        """
        Fit the logistic regression model.
        
        Args:
            X (array-like): Training feature matrix
            y (array-like): Target vector
            feature_names (list, optional): Names of features for interpretation
        
        Returns:
            self: Returns the instance itself
        """
        self.model.fit(X, y)
        self.is_fitted = True
        if feature_names is not None:
            self.feature_names = feature_names
        elif isinstance(X, pd.DataFrame):
            self.feature_names = X.columns.tolist()
        return self
    
    def predict(self, X):
        """
        Predict class labels for samples in X.
        
        Args:
            X (array-like): Feature matrix
        
        Returns:
            array: Predicted class labels
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction")
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """
        Predict class probabilities for samples in X.
        
        Args:
            X (array-like): Feature matrix
        
        Returns:
            array: Predicted class probabilities
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction")
        return self.model.predict_proba(X)
    
    def score(self, X, y, metric='accuracy'):
        """
        Calculate the specified metric for the model.
        
        Args:
            X (array-like): Feature matrix
            y (array-like): True labels
            metric (str): Metric to calculate ('accuracy', 'precision', 'recall', 'f1', 'roc_auc')
        
        Returns:
            float: Score for the specified metric
        """
        y_pred = self.predict(X)
        if metric == 'accuracy':
            return accuracy_score(y, y_pred)
        elif metric == 'precision':
            return precision_score(y, y_pred, average='weighted')
        elif metric == 'recall':
            return recall_score(y, y_pred, average='weighted')
        elif metric == 'f1':
            return f1_score(y, y_pred, average='weighted')
        elif metric == 'roc_auc':
            if len(np.unique(y)) == 2:  # Binary classification
                y_pred_proba = self.predict_proba(X)[:, 1]
                return roc_auc_score(y, y_pred_proba)
            else:  # Multi-class
                return roc_auc_score(y, self.predict_proba(X), multi_class='ovr')
        else:
            raise ValueError(f"Unsupported metric: {metric}")
    
    def get_classification_report(self, X, y):
        """
        Generate a detailed classification report.
        
        Args:
            X (array-like): Feature matrix
            y (array-like): True labels
        
        Returns:
            str: Classification report
        """
        y_pred = self.predict(X)
        return classification_report(y, y_pred)
    
    def plot_confusion_matrix(self, X, y, figsize=(8, 6), cmap='Blues'):
        """
        Plot confusion matrix for the predictions.
        
        Args:
            X (array-like): Feature matrix
            y (array-like): True labels
            figsize (tuple): Figure size
            cmap (str): Color map for the heatmap
        """
        y_pred = self.predict(X)
        cm = confusion_matrix(y, y_pred)
        plt.figure(figsize=figsize)
        sns.heatmap(cm, annot=True, fmt='d', cmap=cmap)
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.show()
    
    def plot_feature_importance(self, figsize=(10, 6)):
        """
        Plot feature importance based on model coefficients.
        
        Args:
            figsize (tuple): Figure size
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before plotting feature importance")
        if self.feature_names is None:
            raise ValueError("Feature names must be provided for plotting importance")
        
        # For multi-class, we'll plot coefficients for each class
        if self.model.coef_.shape[0] > 1:
            n_classes = self.model.coef_.shape[0]
            plt.figure(figsize=(figsize[0], figsize[1] * n_classes))
            for i in range(n_classes):
                plt.subplot(n_classes, 1, i+1)
                plt.bar(self.feature_names, self.model.coef_[i])
                plt.title(f'Feature Importance - Class {i}')
                plt.xlabel('Features')
                plt.ylabel('Coefficient')
                plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            plt.figure(figsize=figsize)
            plt.bar(self.feature_names, self.model.coef_[0])
            plt.title('Feature Importance')
            plt.xlabel('Features')
            plt.ylabel('Coefficient')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
    
    def get_odds_ratios(self):
        """
        Calculate odds ratios from the coefficients.
        
        Returns:
            dict or list: Odds ratios for each feature (dict if feature names available)
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before calculating odds ratios")
        
        odds_ratios = np.exp(self.model.coef_)
        if self.feature_names is not None:
            if odds_ratios.shape[0] > 1:  # Multi-class
                return {f'Class_{i}': dict(zip(self.feature_names, odds)) 
                        for i, odds in enumerate(odds_ratios)}
            else:  # Binary
                return dict(zip(self.feature_names, odds_ratios[0]))
        return odds_ratios
