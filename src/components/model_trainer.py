import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object, evaluate_model

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_array, test_array):
        """
        Train multiple regression models and select the best-performing one based on R^2 score.

        :param train_array: Array containing training data.
        :param test_array: Array containing testing data.
        """
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            # Splitting features and target variables from train and test data
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # Define dictionary of regression models to be trained
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet()
            }

            # Evaluate each model and get model performance metrics
            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)
            logging.info(f'Model Report : {model_report}')

            # Find the best model based on R^2 score
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]

            logging.info(f'Best Model Found, Model Name: {best_model_name}, R^2 Score: {best_model_score}')

            # Get the best model object
            best_model = models[best_model_name]

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            logging.info('Best model saved successfully.')

        except Exception as e:
            logging.error(f'Exception occurred during model training: {e}')
            raise CustomException(e, sys)
