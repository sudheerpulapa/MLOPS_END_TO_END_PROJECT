import os
import sys
import pandas as pd

from src.logger.logging import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

# Initialize DataIngestion to fetch paths for train and test data
data_ingestion = DataIngestion()
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

# Perform data transformation
data_transformation = DataTransformation()
train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path, test_data_path)

# Train the model
model_trainer = ModelTrainer()
model_trainer.initiate_model_training(train_arr, test_arr)

# Evaluate the trained model
model_evaluation = ModelEvaluation()
model_evaluation.initiate_model_evaluation(train_arr, test_arr)
