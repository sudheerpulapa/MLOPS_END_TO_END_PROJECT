import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

# DataIngestionConfig class using dataclass for easy management of file paths
@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

# DataIngestion class to handle the data ingestion process
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            # Reading the dataset from the provided URL
            data = pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/fsdsmendtoend/main/notebooks/data/gemstone.csv")
            logging.info("Successfully read the dataset into a DataFrame")

            # Creating the directory for raw data if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            # Saving the raw data to the specified path
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved the raw dataset in the artifacts folder")

            # Performing train-test split
            logging.info("Performing train-test split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test split completed")

            # Saving the train and test datasets to the specified paths
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Saved the train and test datasets in the artifacts folder")

            # Returning the paths to the train and test datasets
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Error occurred during data ingestion")
            # Raising a custom exception with the error and system information
            raise customexception(e, sys)

# Main block to execute the data ingestion process when the script is run
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
