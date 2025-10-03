"""
Visualization Utilities for Logistic Regression

This module provides functions for creating various plots to help
understand and interpret logistic regression models and data.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc


def plot_sigmoid_function(figsize=(10, 6)):
    """
    Plot the sigmoid function.
    
    Args:
        figsize (tuple): Figure size
    """
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
    
    z = np.linspace(-10, 10, 100)
    sigmoid_values = sigmoid(z)
    
    plt.figure(figsize=figsize)
    plt.plot(z, sigmoid_values)
    plt.title('Sigmoid Function')
    plt.xlabel('z')
    plt.ylabel('σ(z)')
    plt.grid(True)
    plt.show()


def plot_logit_function(figsize=(10, 6)):
    """
    Plot the logit function.
    
    Args:
        figsize (tuple): Figure size
    """
    def logit(p):
        return np.log(p / (1 - p))
    
    p = np.linspace(0.01, 0.99, 100)
    logit_values = logit(p)
    
    plt.figure(figsize=figsize)
    plt.plot(p, logit_values)
    plt.title('Logit Function')
    plt.xlabel('Probability (p)')
    plt.ylabel('logit(p)')
    plt.grid(True)
    plt.show()


def plot_decision_boundary(X, y, model, scaler=None, figsize=(10, 8)):
    """
    Plot decision boundary for a 2D feature space.
    
    Args:
        X (array-like): Feature matrix (must have exactly 2 features)
        y (array-like): Target vector
        model: Trained model with predict method
        scaler: Scaler object if features need scaling
        figsize (tuple): Figure size
    """
    if X.shape[1] != 2:
        raise ValueError("Can only plot decision boundary for 2D feature space")
    
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    grid = np.c_[xx.ravel(), yy.ravel()]
    
    if scaler is not None:
        grid = scaler.transform(grid)
    
    Z = model.predict(grid)
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize=figsize)
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
    plt.title('Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()


def plot_roc_curve(y_true, y_pred_proba, figsize=(8, 6)):
    """
    Plot ROC curve for binary classification.
    
    Args:
        y_true (array-like): True labels
        y_pred_proba (array-like): Predicted probabilities for positive class
        figsize (tuple): Figure size
    """
    fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=figsize)
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.show()


def plot_cost_history(costs, figsize=(10, 6)):
    """
    Plot cost function history during training.
    
    Args:
        costs (list): List of cost values
        figsize (tuple): Figure size
    """
    plt.figure(figsize=figsize)
    plt.plot(costs)
    plt.title('Cost Function During Training')
    plt.xlabel('Iteration')
    plt.ylabel('Cost (Log Loss)')
    plt.grid(True)
    plt.show()


def plot_feature_distribution(X, feature_names=None, figsize=(12, 8)):
    """
    Plot distribution of features.
    
    Args:
        X (array-like): Feature matrix
        feature_names (list, optional): Names of features
        figsize (tuple): Figure size
    """
    if isinstance(X, pd.DataFrame):
        feature_names = X.columns
        X = X.values
    elif feature_names is None:
        feature_names = [f'Feature {i+1}' for i in range(X.shape[1])]
    
    n_features = X.shape[1]
    n_rows = (n_features + 2) // 3  # 3 plots per row
    plt.figure(figsize=(figsize[0], figsize[1] * n_rows))
    
    for i in range(n_features):
        plt.subplot(n_rows, 3, i+1)
        sns.histplot(X[:, i], kde=True)
        plt.title(feature_names[i])
    
    plt.tight_layout()
    plt.show()
