from US_VISA.logger import logging
from US_VISA.exception import USvisaException
import sys

# logging.info("Welcome to Our Major-Project")
logging.info("Checking the exception handling for project")


try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)