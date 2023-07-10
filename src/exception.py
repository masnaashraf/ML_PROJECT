"""import sys

def error_message_details(error,error_detail:sys):
    _, _, exc_tb= error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    #error_message="Error occured in the python script name {0} line number[{1} error message(2)]".format(
    #   file_name,exc_tb.tb_lineno,str(error))
    
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init()__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    
    def __str__(self):
        return self.error_message


    def __str__(self):
        return self.error_message"""


import sys
import logging
import logger

def error_message_details(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in the python script: {0}, line number: {1}, error message: {2}".format(
        file_name, line_number, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
"""
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys) """





