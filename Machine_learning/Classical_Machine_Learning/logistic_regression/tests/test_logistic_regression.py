"""
Unit Tests for Logistic Regression Implementation

This module contains tests for the data processing utilities,
model implementation, and visualization functions.
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification

# Add the parent directory to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.data_processing import split_data, scale_features, handle_imbalanced_data
from src.models.logistic_model import LogisticClassifier


def test_data_splitting():
    """Test data splitting function."""
    X, y = make_classification(n_samples=1000, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    
    assert X_train.shape[0] == 800, "Training set size incorrect"
    assert X_test.shape[0] == 200, "Test set size incorrect"
    assert y_train.shape[0] == 800, "Training labels size incorrect"
    assert y_test.shape[0] == 200, "Test labels size incorrect"
    assert X_train.shape[1] == X.shape[1], "Feature dimension changed"


def test_feature_scaling():
    """Test feature scaling function."""
    X, _ = make_classification(n_samples=1000, n_features=5, random_state=42)
    X_train, X_test, _, _ = split_data(X, _, test_size=0.2, random_state=42)
    
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
    
    assert np.abs(X_train_scaled.mean(axis=0)).mean() < 1e-6, "Scaled training data mean not close to 0"
    assert np.abs(X_train_scaled.std(axis=0) - 1).mean() < 1e-6, "Scaled training data std not close to 1"
    assert X_train_scaled.shape == X_train.shape, "Scaled training data shape mismatch"
    assert X_test_scaled.shape == X_test.shape, "Scaled test data shape mismatch"


def test_imbalanced_data_handling():
    """Test handling of imbalanced data with SMOTE."""
    X, y = make_classification(n_samples=1000, n_features=5, weights=[0.9, 0.1], random_state=42)
    X_resampled, y_resampled = handle_imbalanced_data(X, y, random_state=42)
    
    assert len(np.unique(y_resampled, return_counts=True)[1]) == 2, "Incorrect number of classes after resampling"
    class_counts = np.unique(y_resampled, return_counts=True)[1]
    assert abs(class_counts[0] - class_counts[1]) < 10, "Classes not balanced after SMOTE"


def test_model_training_and_prediction():
    """Test model training and prediction."""
    X, y = make_classification(n_samples=1000, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    X_train_scaled, X_test_scaled, _ = scale_features(X_train, X_test)
    
    model = LogisticClassifier()
    model.fit(X_train_scaled, y_train)
    
    assert model.is_fitted, "Model not marked as fitted"
    predictions = model.predict(X_test_scaled)
    assert len(predictions) == len(y_test), "Prediction length mismatch"
    assert set(np.unique(predictions)).issubset(set(np.unique(y_train))), "Invalid prediction values"
    
    accuracy = model.score(X_test_scaled, y_test, metric='accuracy')
    assert 0 <= accuracy <= 1, "Accuracy out of range"


def test_model_metrics():
    """Test various model metrics."""
    X, y = make_classification(n_samples=1000, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    X_train_scaled, X_test_scaled, _ = scale_features(X_train, X_test)
    
    model = LogisticClassifier()
    model.fit(X_train_scaled, y_train)
    
    metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    for metric in metrics:
        score = model.score(X_test_scaled, y_test, metric=metric)
        assert 0 <= score <= 1, f"{metric} out of range"


def test_model_with_dataframe():
    """Test model with pandas DataFrame input."""
    X, y = make_classification(n_samples=1000, n_features=5, random_state=42)
    feature_names = [f'feature_{i}' for i in range(X.shape[1])]
    X_df = pd.DataFrame(X, columns=feature_names)
    y_series = pd.Series(y)
    
    X_train, X_test, y_train, y_test = split_data(X_df, y_series, test_size=0.2, random_state=42)
    X_train_scaled, X_test_scaled, _ = scale_features(X_train, X_test)
    
    model = LogisticClassifier()
    model.fit(X_train_scaled, y_train)
    
    assert model.feature_names == feature_names, "Feature names not stored correctly"
    predictions = model.predict(X_test_scaled)
    assert len(predictions) == len(y_test), "Prediction length mismatch"

if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
