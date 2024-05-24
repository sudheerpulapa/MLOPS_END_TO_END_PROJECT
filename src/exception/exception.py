import sys

class CustomException(Exception):
    """
    Custom exception class to capture and provide detailed error information.
    """

    def __init__(self, error_message, error_details: sys):
        """
        Initialize the custom exception with error message and details.

        :param error_message: The error message to be displayed.
        :param error_details: The sys module to extract error details.
        """
        # Assign the error message to an instance variable
        self.error_message = error_message

        # Extract traceback information from the exception details
        _, _, exc_tb = error_details.exc_info()

        # Print the traceback object for debugging (optional, can be removed)
        print(exc_tb)

        # Extract the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno

        # Extract the file name where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        """
        String representation of the custom exception, including the file name,
        line number, and error message.
        """
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )


if __name__ == "__main__":
    try:
        # Example code to trigger an exception (division by zero)
        a = 1 / 0

    except Exception as e:
        # Raise the custom exception with the original exception and sys module
        raise CustomException(e, sys)
