import sys
import logging

def error_message_detail(error, error_detail: sys):
    # exc_info returns (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract filename and line number from the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Corrected string formatting with proper closing parenthesis
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # 1. Corrected super() call
        # 2. We pass the message to the parent Exception class
        super().__init__(error_message)
        
        # 3. Generate the detailed message using our helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


