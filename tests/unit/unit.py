import os
import sys
import pandas as pd
from src.logger.logging import logging
from src.exception.exception import customexception
import numpy as np
import pickle

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def save_object(file_path, obj):
    """
    Save a Python object to a file using pickle.

    :param file_path: Path to save the object.
    :param obj: Python object to be saved.
    """
    try:
        # Create directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Save object to file
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        # Catch any exceptions, log them, and raise a custom exception
        logging.error(f"An error occurred while saving object: {e}")
        raise customexception(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    """
    Evaluate the performance of multiple models.

    :param X_train: Training features.
    :param y_train: Training labels.
    :param X_test: Testing features.
    :param y_test: Testing labels.
    :param models: Dictionary of models to evaluate.
    :return: Dictionary containing model names and their R2 scores on test data.
    """
    try:
        report = {}
        for model_name, model in models.items():
            # Train model
            model.fit(X_train, y_train)

            # Predict Testing data
            y_test_pred = model.predict(X_test)

            # Get R2 scores for test data
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score

        return report

    except Exception as e:
        # Catch any exceptions, log them, and raise a custom exception
        logging.error(f"An error occurred during model evaluation: {e}")
        raise customexception(e, sys)

def load_object(file_path):
    """
    Load a Python object from a file using pickle.

    :param file_path: Path to the file containing the object.
    :return: Loaded Python object.
    """
    try:
        # Load object from file
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        # Catch any exceptions, log them, and raise a custom exception
        logging.error(f"An error occurred while loading object: {e}")
        raise customexception(e, sys)
