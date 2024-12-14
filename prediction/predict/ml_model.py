import joblib
import numpy as np

class PostQualityPredictor:
    def predict(self, reputation, interactions):
        # Load saved model
        model = joblib.load('ml_model.joblib')

        # Prepare input
        input_data = np.array([[reputation, interactions]])
        
        # Predict
        prediction = model.predict(input_data)[0]
        return round(prediction, 2)