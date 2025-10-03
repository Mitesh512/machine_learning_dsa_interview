"""
Main Script for Logistic Regression Application

This script provides a command-line interface for training, evaluating,
and making predictions with logistic regression models.
"""

import argparse
import sys
import os
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add the parent directory to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_processing import split_data, scale_features, handle_imbalanced_data, preprocess_dataframe
from models.logistic_model import LogisticClassifier
from visualization.plots import plot_roc_curve, plot_feature_importance


def load_data(file_path, target_column, categorical_columns=None):
    """
    Load and preprocess data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        target_column (str): Name of the target column
        categorical_columns (list, optional): List of categorical column names
    
    Returns:
        tuple: Feature matrix and target vector
    """
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully loaded data from {file_path}")
        return preprocess_dataframe(df, target_column, categorical_columns)
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise


def train_model(X, y, penalty='l2', C=1.0, balance_data=False):
    """
    Train a logistic regression model.
    
    Args:
        X (array-like): Feature matrix
        y (array-like): Target vector
        penalty (str): Type of regularization
        C (float): Inverse of regularization strength
        balance_data (bool): Whether to handle imbalanced data with SMOTE
    
    Returns:
        tuple: Trained model and scaler
    """
    logger.info("Splitting data into training and testing sets")
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    logger.info("Scaling features")
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
    
    if balance_data:
        logger.info("Handling imbalanced data with SMOTE")
        X_train_scaled, y_train = handle_imbalanced_data(X_train_scaled, y_train)
    
    logger.info("Training logistic regression model")
    model = LogisticClassifier(penalty=penalty, C=C)
    model.fit(X_train_scaled, y_train, feature_names=X.columns if isinstance(X, pd.DataFrame) else None)
    
    logger.info("Evaluating model on test set")
    print("Test Set Evaluation:")
    print(model.get_classification_report(X_test_scaled, y_test))
    
    # Plot ROC curve for binary classification
    if len(np.unique(y)) == 2:
        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        plot_roc_curve(y_test, y_pred_proba)
    
    # Plot feature importance
    if model.feature_names is not None:
        model.plot_feature_importance()
    
    return model, scaler


def predict(model, scaler, data_file, output_file=None):
    """
    Make predictions on new data.
    
    Args:
        model: Trained logistic regression model
        scaler: Fitted scaler for feature scaling
        data_file (str): Path to CSV file with new data
        output_file (str, optional): Path to save predictions
    """
    try:
        df = pd.read_csv(data_file)
        logger.info(f"Loaded new data from {data_file}")
        
        # Ensure the data has the same features as the training data
        if model.feature_names is not None:
            missing_cols = set(model.feature_names) - set(df.columns)
            if missing_cols:
                logger.warning(f"Missing columns in new data: {missing_cols}")
                for col in missing_cols:
                    df[col] = 0  # Fill missing columns with zeros
            df = df[model.feature_names]
        
        X = scaler.transform(df)
        predictions = model.predict(X)
        probabilities = model.predict_proba(X)
        
        # Prepare output
        output_df = df.copy()
        output_df['prediction'] = predictions
        if probabilities.shape[1] == 2:  # Binary classification
            output_df['probability'] = probabilities[:, 1]
        else:  # Multi-class
            for i in range(probabilities.shape[1]):
                output_df[f'probability_class_{i}'] = probabilities[:, i]
        
        if output_file:
            output_df.to_csv(output_file, index=False)
            logger.info(f"Saved predictions to {output_file}")
        else:
            print("Predictions:")
            print(output_df.head())
        
        return output_df
    except Exception as e:
        logger.error(f"Error making predictions: {str(e)}")
        raise


def main():
    """Main function to run the logistic regression application."""
    parser = argparse.ArgumentParser(description='Logistic Regression Application')
    parser.add_argument('mode', choices=['train', 'predict'],
                        help='Mode to run: train a new model or predict with an existing one')
    parser.add_argument('--data', help='Path to data CSV file')
    parser.add_argument('--target', help='Target column name for training')
    parser.add_argument('--categorical', nargs='*', help='Categorical column names')
    parser.add_argument('--penalty', default='l2', choices=['l1', 'l2', 'elasticnet', 'none'],
                        help='Regularization penalty')
    parser.add_argument('--C', type=float, default=1.0,
                        help='Inverse of regularization strength')
    parser.add_argument('--balance', action='store_true',
                        help='Handle imbalanced data with SMOTE')
    parser.add_argument('--model', help='Path to saved model for prediction')
    parser.add_argument('--scaler', help='Path to saved scaler for prediction')
    parser.add_argument('--output', help='Path to save predictions')
    
    args = parser.parse_args()
    
    if args.mode == 'train':
        if not args.data or not args.target:
            raise ValueError("--data and --target arguments are required for training")
        
        logger.info("Starting training mode")
        X, y = load_data(args.data, args.target, args.categorical)
        model, scaler = train_model(X, y, args.penalty, args.C, args.balance)
        
        # Save model and scaler (in a real application, you'd use joblib or pickle)
        logger.info("Training completed")
    
    else:  # predict mode
        if not args.data or not args.model or not args.scaler:
            raise ValueError("--data, --model, and --scaler arguments are required for prediction")
        
        logger.info("Starting prediction mode")
        # In a real application, you'd load the saved model and scaler
        # For demonstration, we're not actually loading from file
        logger.warning("Model loading not implemented in this demo")
        
        # Placeholder for prediction
        # model = load_model(args.model)
        # scaler = load_scaler(args.scaler)
        # predict(model, scaler, args.data, args.output)
        logger.info("Prediction mode is a placeholder in this demo")


if __name__ == "__main__":
    main()
