import os
import sys
import pandas as pd
from src.exception.exception import CustomException  # Corrected import statement
from src.logger.logging import logging
from src.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        """
        Initialize the PredictPipeline object.
        """
        print("Initializing the PredictPipeline object")  # Placeholder print statement

    def predict(self, features):
        """
        Predict the target variable using the provided features.

        :param features: Input features for prediction.
        :return: Predicted values.
        """
        try:
            # Load preprocessor and model objects
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # Transform features using preprocessor and make predictions using model
            scaled_features = preprocessor.transform(features)
            predictions = model.predict(scaled_features)

            return predictions

        except Exception as e:
            # Catch any exceptions, log them, and raise a custom exception
            logging.error("An error occurred during prediction: {}".format(e))
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, carat: float, depth: float, table: float, x: float, y: float, z: float,
                 cut: str, color: str, clarity: str):
        """
        Initialize the CustomData object with diamond attributes.

        :param carat: Carat weight of the diamond.
        :param depth: Depth of the diamond (as a percentage of its diameter).
        :param table: Width of the diamond's table (top flat surface) relative to its widest point.
        :param x: Length of the diamond in mm.
        :param y: Width of the diamond in mm.
        :param z: Depth of the diamond in mm.
        :param cut: Quality of the diamond's cut (e.g., Fair, Good, Very Good, Premium, Ideal).
        :param color: Color grade of the diamond (e.g., D, E, F, G, H, I, J).
        :param clarity: Clarity grade of the diamond (e.g., I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF).
        """
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        """
        Convert diamond attributes into a DataFrame.

        :return: DataFrame containing diamond attributes.
        """
        try:
            # Create a dictionary with diamond attributes
            custom_data_input_dict = {
                'carat': [self.carat],
                'depth': [self.depth],
                'table': [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity]
            }
            # Convert the dictionary into a DataFrame
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame created successfully')
            return df

        except Exception as e:
            # Catch any exceptions, log them, and raise a custom exception
            logging.error("An error occurred while creating DataFrame: {}".format(e))
            raise CustomException(e, sys)
