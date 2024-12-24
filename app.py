from sing_language_detection.logger import logging

# logging.info("Welcome to the Project")

# now writing a demo for excetion

from sing_language_detection.exception import SignExceptioin
import sys

try:
    a = 7/'9'
except Exception as e:
    raise SignExceptioin(e, sys) from e