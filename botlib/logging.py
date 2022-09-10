
from enum import Enum

import time

class LoggingLevel(Enum):
    INFO = 1
    LOG = 2
    WARN = 3
    ERROR = 4

class ConsoleLogger:

    def __init__(self, logging_level = LoggingLevel.LOG):
        self.logging_level = logging_level

    def log(self, msg):
        if self.logging_level.value <= LoggingLevel.LOG.value :
            print(ConsoleLogger.add_time(msg))
    
    def info(self, msg):
        if self.logging_level.value <= LoggingLevel.INFO.value :
            print(ConsoleLogger.add_time(msg))

    @staticmethod
    def add_time(msg):
        return "["+time.asctime()+"] : "+str(msg) 
    
Logger = ConsoleLogger()


