import logging
import os
from datetime import datetime

# Define the log file name based on the current datetime to ensure uniqueness
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the log directory path within the current working directory
log_path = os.path.join(os.getcwd(), "logs")

# Create the log directory if it does not exist
os.makedirs(log_path, exist_ok=True)

# Define the complete log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    filename=LOG_FILEPATH,  # Log messages will be written to the specified file
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"  # Define the log message format
)

# Example usage of the logger
logging.info("Logging setup is complete and the logger is configured.")
logging.info("This is a test log message to ensure everything is working correctly.")

# Example function to demonstrate logging in different parts of the application
def example_function():
    logging.info("This is an info message from example_function.")
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error("An error occurred: %s", e)

# Call the example function to generate log entries
example_function()
