import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
class PostQualityPredictor:
    def __init__(self, model_path='post_quality_model.joblib'):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = ['user_reputation', 'taker_mpxr_delta']
        self.model_path = model_path
    
    def load_model(self, path):
        """Load saved model and scaler"""
        try:
            model_artifacts = joblib.load(path)
            self.model = model_artifacts['model']
            self.scaler = model_artifacts['scaler']
            self.feature_names = model_artifacts['feature_names']
            print("Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
    
    def predict(self, user_reputation, taker_mpxr_delta):
        #load model
        self.load_model(self.model_path)

        """Make predictions for new data"""
        if self.model is None:
            print("Model not trained or loaded")
            return None

        input_features = pd.DataFrame({
            'user_reputation': [user_reputation],
            'taker_mpxr_delta': [taker_mpxr_delta]
        })

        scaled_features = self.scaler.transform(input_features)
        prediction = self.model.predict(scaled_features)[0]
        return prediction