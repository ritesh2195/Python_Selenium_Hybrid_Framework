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

        if actualTitle == "Your store. Login":

            self.logger.info("****Home Page Test is passed****")

            assert True

        else:

            allure.attach(self.driver.get_screenshot_as_png(), name="loginScreen", attachment_type=AttachmentType.PNG)

            self.logger.info("****Home Page Test is failed****")

            self.driver.save_screenshot('.\\Screenshots\\' + 'homePage.png')

            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_login(self):

        self.logger.info("*********Login Test Started***********")

        self.logger.info("********Verifying Logim Function***********")

        self.lp = Login(self.driver)

        self.lp.doLogin(self.Email, self.Password)

        actualTitle = self.driver.title

        if actualTitle == "Dashboard / nopCommerce administration":

            self.logger.info("****Login Function is Passed****")

            assert True

        else:

            self.driver.save_screenshot('D:\\PYTHON\\nopCommerce\\Screenshots\\abc.png')

            self.logger.info("****Login Function is Failed****")

            assert False
