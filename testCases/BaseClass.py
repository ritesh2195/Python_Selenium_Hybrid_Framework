import inspect
from datetime import datetime

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

    def captureScreenshot(self):

        currTime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        screenshotName = 'test' + '_' + currTime

        self.driver.save_screenshot(".\\Screenshots\\" + screenshotName + '.png')
