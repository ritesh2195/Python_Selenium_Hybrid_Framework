import inspect
import pytest
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file.setFormatter(formatter)
        fileHandler = logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger