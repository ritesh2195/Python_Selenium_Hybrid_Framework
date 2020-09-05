import inspect
import logging


class LogGen:
    @staticmethod
    def loggen():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file = logging.FileHandler('.\\Logs\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file.setFormatter(formatter)
        fileHandler = logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger
