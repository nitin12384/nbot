
from enum import Enum

import time

_log_file_path = "./botFiles/log.txt"

_log_into_file_default = True

class LoggingLevel(Enum):
    INFO = 1
    LOG = 2
    WARN = 3
    ERROR = 4

class Logger:

    def __init__(self, logging_level = LoggingLevel.LOG):
        self.logging_level = logging_level
        self.log_file = open(_log_file_path, 'w')

    def _do_logging(self, msg, file_logging):
        if file_logging:
            self.log_file.write(Logger.add_time(msg))
        else :
            print(Logger.add_time(msg))

    def log(self, msg, file_logging=_log_into_file_default):
        if self.logging_level.value <= LoggingLevel.LOG.value :
            self._do_logging("[LOG]"+msg, file_logging)
    
    def info(self, msg, file_logging=_log_into_file_default):
        if self.logging_level.value <= LoggingLevel.INFO.value :
            self._do_logging("[INFO]"+msg, file_logging)



    @staticmethod
    def add_time(msg):
        return "["+time.asctime()+"] : "+str(msg) 

Logger = Logger()


