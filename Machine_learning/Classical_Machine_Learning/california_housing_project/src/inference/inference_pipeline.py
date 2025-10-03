import joblib
import pandas as pd
from pathlib import Path

class InferencePipeline:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = None
        self.selected_features = None
        self.load_artifacts()
        
    def load_artifacts(self):
        """Load the trained model and preprocessing objects"""
        model_path = Path(self.config.MODEL_ARTIFACTS_DIR) / "model.joblib"
        scaler_path = Path(self.config.MODEL_ARTIFACTS_DIR) / "scaler.joblib"
        
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        
    def preprocess_input(self, input_data):
        """Preprocess the input data"""
        # Convert input to DataFrame if it's not already
        if not isinstance(input_data, pd.DataFrame):
            input_data = pd.DataFrame(input_data)
            
        # Scale features
        scaled_data = self.scaler.transform(input_data)
        scaled_df = pd.DataFrame(scaled_data, columns=input_data.columns)
        
        return scaled_df
        
    def predict(self, input_data):
        """Make predictions on input data"""
        # Preprocess input
        processed_data = self.preprocess_input(input_data)
        
        # Make predictions
        predictions = self.model.predict(processed_data)
        
        return predictions
