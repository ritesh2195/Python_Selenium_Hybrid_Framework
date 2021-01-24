from abc import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class page(ABC):

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(self.driver, 15)

    @abstractmethod
    def getPageTitle(self):
        pass

    @abstractmethod
    def waitForElementPresent(self, locator):
        pass

    @abstractmethod
    def elementToClickable(self, locator):
        pass