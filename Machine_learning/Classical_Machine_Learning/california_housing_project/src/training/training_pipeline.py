import mlflow
import joblib
from pathlib import Path
from ..data.data_processor import DataProcessor
from ..features.feature_selector import FeatureSelector
from ..training.model_trainer import ModelTrainer

class TrainingPipeline:
    def __init__(self, config):
        self.config = config
        self.data_processor = DataProcessor(random_state=config.RANDOM_STATE)
        self.scaler = self.data_processor.scaler
        self.feature_selector = FeatureSelector()
        self.model_trainer = ModelTrainer(random_state=config.RANDOM_STATE)
        
    def run(self):
        """Run the training pipeline"""
        mlflow.start_run()
        try:
            # Load and process data
            df = self.data_processor.load_data()
            X_train, X_test, y_train, y_test = self.data_processor.preprocess_data(df)
            
            # Feature selection
            X_train = self.feature_selector.select_features_univariate(X_train, y)
            X_test = X_test[X_train.columns]
            
            # Optimize hyperparameters
            best_params = self.model_trainer.optimize_hyperparameters(X_train, X_test, y_train, y_test)
            
            # Train model with best parameters
            model = self.model_trainer.train_model(X_train, y_train, best_params)
            
            # Evaluate model
            metrics = self.model_trainer.evaluate_model(model, X_test, y_test)
            
            # Log metrics and parameters
            mlflow.log_params(best_params)
            mlflow.log_metrics(metrics)
            
            # Save model and preprocessing objects
            model_path = Path(self.config.MODEL_ARTIFACTS_DIR) / "model.joblib"
            scaler_path = Path(self.config.MODEL_ARTIFACTS_DIR) / "scaler.joblib"
            
            joblib.dump(model, model_path)
            joblib.dump(self.data_processor.scaler, scaler_path)
            
            mlflow.log_artifact(model_path)
            mlflow.log_artifact(scaler_path)
            
            return metrics
            
        finally:
            mlflow.end_run()
