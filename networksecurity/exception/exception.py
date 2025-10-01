import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
        def __init__(self,error_massage,error_detail:sys):
                self.error_message=error_massage
                _,_,exc_tb=error_detail.exc_info()


                self.linevo=exc_tb.tb_lineno
                self.file_name=exc_tb.tb_frame.f_code.co_filename

        def __str__(self):
                return "Error occured in python script name [{0}] line number [{1}] error massege [{2}]".format(
                self.file_name,self.linevo,str(self.error_message))


# if __name__=='__main__':
#         try:
#                 logger.logging.info("Enter the try block")
#                 a=1/0
#                 print("This will be not printed",a)
#         except Exception as e:
#                 raise NetworkSecurityException(e,sys)