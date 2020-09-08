import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    Email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("*********Home Page Test Started***********")

        self.logger.info("********Verifying HomePage Title***********")

        self.driver = setup

        self.driver.maximize_window()

        self.driver.get(self.baseURL)

        actualTitle=self.driver.title

        self.driver.close()

        if actualTitle == "Your store. Login":

            self.logger.info("****Home Page Test is passed****")

            assert True

        else:

            self.logger.info("****Home Page Test is failed****")

            self.driver.save_screenshot('.\\Screenshots\\'+'homePage.png')

            assert False

    def test_login(self,setup):

        self.logger.info("*********Login Test Started***********")

        self.logger.info("********Verifying Logim Function***********")

        self.driver = setup

        self.driver.get(self.baseURL)

        self.lp=Login(self.driver)

        self.lp.setEmail(self.Email)

        self.lp.setPassword(self.Password)

        self.lp.clickLogin()

        actualTitle = self.driver.title

        self.driver.close()

        if actualTitle == "Dashboard / nopCommerce administration":

            self.logger.info("****Login Function is Passed****")

            assert True

        else:
            self.driver.save_screenshot('D:\\PYTHON\\nopCommerce\\Screenshots\\abc.png')

            self.logger.info("****Login Function is Failed****")

            assert False

        self.driver.close()


