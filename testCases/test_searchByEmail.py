import time

from pageObjects.SearchCustomer import searchCustomer
from testCases.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.AddCustomePage import addCustomer
from pageObjects.LoginPage import Login
import pytest


class TestSearch_004(BaseClass):
    baseURL = ReadConfig.getApplicationURL()

    Email = ReadConfig.getEmail()

    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchgCustomer(self, setup):
        # self.driver = setup

        self.lp = Login(self.driver)

        self.lp.setEmail(self.Email)

        self.lp.setPassword(self.Password)

        self.lp.clickLogin()

        self.addCust = addCustomer(self.driver)

        self.addCust.clickCustomers()

        self.addCust.clickCustomersMenu()

        self.search = searchCustomer(self.driver)

        self.search.setEmail("victoria_victoria@nopCommerce.com")

        self.search.clickSearch()

        status = self.search.searchByEmail("victoria_victoria@nopCommerce.com")

        assert True == status

        time.sleep(3)

        # self.driver.close()
