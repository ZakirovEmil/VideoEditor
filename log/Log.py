from os import path
from settings import *


class Log:
    @staticmethod
    def write(text):
        with open(PATH_LOGS, 'a') as log:
            log.write(text + "\n")