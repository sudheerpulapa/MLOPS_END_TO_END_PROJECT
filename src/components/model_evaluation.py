import os
import sys
import mlflow
import mlflow.sklearn
import numpy as np
from src.utils.utils import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.logger.logging import logging
from src.exception.exception import CustomException

class ModelEvaluation:
    def __init__(self):
        logging.info("Evaluation started")

    def eval_metrics(self, actual, pred):
        """
        Calculate evaluation metrics (RMSE, MAE, R2) based on actual and predicted values.

        :param actual: Actual target values.
        :param pred: Predicted target values.
        :return: Tuple containing RMSE, MAE, and R2 scores.
        """
        rmse = np.sqrt(mean_squared_error(actual, pred))  # Root Mean Squared Error
        mae = mean_absolute_error(actual, pred)  # Mean Absolute Error
        r2 = r2_score(actual, pred)  # R^2 Score
        logging.info("Evaluation metrics captured")
        return rmse, mae, r2

    def initiate_model_evaluation(self, train_array, test_array):
        """
        Evaluate the trained model using test data and log evaluation metrics.

        :param train_array: Training data array.
        :param test_array: Testing data array.
        """
        try:
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            # Load the trained model
            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)

            # Start MLflow run
            with mlflow.start_run():
                logging.info("Model evaluation initiated")

                # Make predictions using the test data
                predictions = model.predict(X_test)

                # Calculate evaluation metrics
                rmse, mae, r2 = self.eval_metrics(y_test, predictions)

                # Log evaluation metrics
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("r2", r2)

                # Determine the tracking URL type (e.g., file, http, etc.)
                tracking_url_type = urlparse(mlflow.get_tracking_uri()).scheme

                # If using a file-based store, log the model without registering it
                if tracking_url_type == "file":
                    mlflow.sklearn.log_model(model, "model")
                    logging.info("Model logged to MLflow without model registration")
                else:
                    # Register the model with the MLflow Model Registry
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                    logging.info("Model registered and logged to MLflow Model Registry")

        except Exception as e:
            logging.error("Exception occurred during model evaluation: {}".format(e))
            raise CustomException(e, sys)
