import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.NORMAL)
class Test_001_login(BaseClass):

    baseURL = ReadConfig.getApplicationURL()
    Email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.MINOR)
    def test_homePageTitle(self, setup):

        self.logger.info("*********Home Page Test Started***********")

        self.logger.info("********Verifying HomePage Title***********")

        actualTitle = self.driver.title

        assert actualTitle == "Your store. Login"

    @allure.severity(allure.severity_level.MINOR)
    def test_login(self):

        self.logger.info("*********Login Test Started***********")

        self.logger.info("********Verifying Logim Function***********")

        self.lp = Login(self.driver)

        self.lp.doLogin(self.Email, self.Password)

        userName = self.lp.getUserName()

        actualTitle = self.lp.getTitle()

        assert actualTitle == "Dashboard / nopCommerce administration"

        assert userName == 'John Smith'



