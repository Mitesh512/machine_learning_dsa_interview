import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import joblib
import os

class DataProcessor:
    def __init__(self, random_state=42):
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.encoders = {}  # Dictionary to store one encoder per categorical column
        self.data_path = "/Users/mitesh1.gupta/Documents/New_Learning/Machine_learning/california_housing_project/data/housing.csv"
        self.model_dir = "/Users/mitesh1.gupta/Documents/New_Learning/Machine_learning/california_housing_project/models"
        
    def load_data(self):
        """Load California Housing dataset"""
        df = pd.read_csv(self.data_path)
        df.rename(columns={"median_house_value":"target"}, inplace=True)
        return df
    
    def preprocess_data(self, df, categorical_columns=None, is_training=True):
        """Preprocess the data with consistent one-hot encoding for categorical columns
        
        Args:
            df (pd.DataFrame): Input dataframe
            categorical_columns (list): List of column names to one-hot encode
            is_training (bool): Whether this is training data or test/inference data
        """
        # Handle missing values if any
        df = df.dropna()
        
        # Split features and target
        X = df.drop('target', axis=1)
        y = df['target']
        
        # Perform one-hot encoding if categorical columns are specified
        if categorical_columns:
            X = self.one_hot_encode(X, categorical_columns, is_training)
        
        if is_training:
            X_train, X_test, y_train, y_test = self.split_data(X, y)
            
            # Scale only numeric columns
            numeric_columns = X.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_columns) > 0:
                X_train[numeric_columns] = self.scaler.fit_transform(X_train[numeric_columns])
                X_test[numeric_columns] = self.scaler.transform(X_test[numeric_columns])
            
            # Save preprocessors for future use
            self.save_preprocessors()
            
            return X_train, X_test, y_train, y_test
        else:
            # For inference, apply scaling using saved scaler
            numeric_columns = X.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_columns) > 0:
                X[numeric_columns] = self.scaler.transform(X[numeric_columns])
            return X
    
    def one_hot_encode(self, X, categorical_columns, is_training=True):
        """One-hot encode categorical columns with handling for unknown categories
        
        Args:
            X (pd.DataFrame): Input features
            categorical_columns (list): List of column names to encode
            is_training (bool): Whether this is training data or test/inference data
        """
        X = X.copy()
        
        for col in categorical_columns:
            if is_training:
                # During training, fit and transform
                encoder = OneHotEncoder(sparse=False, handle_unknown='ignore', drop='first')
                encoded_features = encoder.fit_transform(X[[col]])
                self.encoders[col] = encoder
            else:
                # During inference, use saved encoder
                encoder = self.encoders[col]
                encoded_features = encoder.transform(X[[col]])
            
            # Get feature names from encoder
            feature_names = [f"{col}_{cat}" for cat in encoder.get_feature_names_out([col])]
            
            # Convert to DataFrame with proper column names
            encoded_df = pd.DataFrame(
                encoded_features,
                columns=feature_names,
                index=X.index
            )
            
            # Add encoded columns to original dataframe
            X = pd.concat([X.drop(col, axis=1), encoded_df], axis=1)
        
        return X
    
    def save_preprocessors(self):
        """Save preprocessors (scaler and encoders) for future use"""
        os.makedirs(self.model_dir, exist_ok=True)
        
        # Save scaler
        joblib.dump(self.scaler, os.path.join(self.model_dir, 'scaler.joblib'))
        
        # Save encoders
        for col, encoder in self.encoders.items():
            joblib.dump(encoder, os.path.join(self.model_dir, f'encoder_{col}.joblib'))
    
    def load_preprocessors(self):
        """Load saved preprocessors for inference"""
        # Load scaler
        scaler_path = os.path.join(self.model_dir, 'scaler.joblib')
        if os.path.exists(scaler_path):
            self.scaler = joblib.load(scaler_path)
        
        # Load encoders
        self.encoders = {}
        for file in os.listdir(self.model_dir):
            if file.startswith('encoder_') and file.endswith('.joblib'):
                col = file[8:-7]  # Remove 'encoder_' prefix and '.joblib' suffix
                self.encoders[col] = joblib.load(os.path.join(self.model_dir, file))
    
    def split_data(self, X, y, test_size=0.2):
        """Split data into train and test sets"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )
        return X_train, X_test, y_train, y_test
