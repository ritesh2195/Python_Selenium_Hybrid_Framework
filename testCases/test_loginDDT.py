import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtil

class Test_002_loginDDT:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/nopCommerce.xlsx"

    logger=LogGen.loggen()

    def test_login(self,setup):

        self.logger.info("*********Login Test Test_002 Started***********")

        self.logger.info("********Verifying Logim Function***********")

        self.driver = setup

        self.driver.maximize_window()

        self.driver.get(self.baseURL)

        self.lp=Login(self.driver)

        self.rows=XLUtil.getRowCount(self.path,'Sheet1')

        list_status=[]

        for r in range(2,self.rows+1):

            self.email=XLUtil.readData(self.path,'Sheet1',r,1)

            self.password=XLUtil.readData(self.path,'Sheet1',r,2)

            self.exp=XLUtil.readData(self.path,'Sheet1',r,3)

            self.lp.setEmail(self.email)

            self.lp.setPassword(self.password)

            self.lp.clickLogin()

            time.sleep(5)

            actualTitle=self.driver.title

            expTitle="Dashboard / nopCommerce administration"

            if actualTitle==expTitle:

                if self.exp=="pass":

                    self.logger.info("passed")

                    self.lp.clickLogout()

                    list_status.append("pass")

                elif self.exp=="fail":

                    self.logger.info("failed")

                    self.lp.clickLogout()

                    list_status.append("fail")

            elif actualTitle!=expTitle:

                if self.exp=="pass":

                    self.logger.info("failed")

                    list_status.append("fail")

                elif self.exp=="fail":

                    self.logger.info("pass")

                    list_status.append("pass")

        if "fail" not in list_status:
            self.driver.close()

            assert True

        else:

            self.driver.close()

            assert False
