"""
Data Processing Utilities for Logistic Regression

This module provides functions for preprocessing data before training
or inference with logistic regression models.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets.
    
    Args:
        X (array-like): Feature matrix
        y (array-like): Target vector
        test_size (float): Proportion of dataset to include in the test split
        random_state (int): Random state for reproducibility
    
    Returns:
        tuple: Training and testing sets (X_train, X_test, y_train, y_test)
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def scale_features(X_train, X_test=None):
    """
    Scale features using StandardScaler.
    
    Args:
        X_train (array-like): Training feature matrix
        X_test (array-like, optional): Testing feature matrix
    
    Returns:
        tuple or array: Scaled training data and testing data if provided
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    if X_test is not None:
        X_test_scaled = scaler.transform(X_test)
        return X_train_scaled, X_test_scaled, scaler
    return X_train_scaled, scaler


def handle_imbalanced_data(X, y, random_state=42):
    """
    Handle imbalanced data using SMOTE (Synthetic Minority Oversampling Technique).
    
    Args:
        X (array-like): Feature matrix
        y (array-like): Target vector
        random_state (int): Random state for reproducibility
    
    Returns:
        tuple: Resampled feature matrix and target vector
    """
    smote = SMOTE(random_state=random_state)
    return smote.fit_resample(X, y)


def preprocess_dataframe(df, target_column, categorical_columns=None):
    """
    Preprocess a dataframe by encoding categorical variables and handling missing values.
    
    Args:
        df (pandas.DataFrame): Input dataframe
        target_column (str): Name of the target column
        categorical_columns (list, optional): List of categorical column names
    
    Returns:
        tuple: Processed feature matrix and target vector
    """
    # Make a copy to avoid modifying the original
    df_processed = df.copy()
    
    # Handle missing values
    df_processed = df_processed.fillna(df_processed.mean())
    
    # Separate features and target
    X = df_processed.drop(target_column, axis=1)
    y = df_processed[target_column]
    
    # Encode categorical variables if any
    if categorical_columns:
        for col in categorical_columns:
            if col in X.columns:
                le = LabelEncoder()
                X[col] = le.fit_transform(X[col])
    
    return X, y
