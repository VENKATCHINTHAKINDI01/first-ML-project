import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            # Use os.path.join for cross-platform compatibility
            model_path = os.path.join('artifacts', 'model.pkl')
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            # Load model and preprocessor
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Scale the features using the preprocessor
            data_scaled = preprocessor.transform(features)

            # Predict using the model
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            # Provide detailed error message for better traceability
            raise CustomException(f"Error in PredictPipeline during prediction: {str(e)}", sys)


class CustomData:
    def __init__(self, 
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        """
        Class to handle custom data input for predictions.
        """
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        """
        Converts the custom data into a pandas DataFrame for prediction.
        """
        try:
            # Dictionary to store the data
            custom_data_input_dict = {
                'gender': [self.gender],
                'race/ethnicity': [self.race_ethnicity],
                'parental level of education': [self.parental_level_of_education],
                'lunch': [self.lunch],
                'test preparation course': [self.test_preparation_course],
                'reading score': [self.reading_score],
                'writing score': [self.writing_score],
            }

            # Create DataFrame from the dictionary
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            # Handle any exception that occurs
            raise CustomException(f"Error in CustomData when creating DataFrame: {str(e)}", sys)
