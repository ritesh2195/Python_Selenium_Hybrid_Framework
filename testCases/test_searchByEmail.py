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

    searchEmail = ReadConfig.getsearchEmail()

    logger = LogGen.loggen()

    def test_searchgCustomer(self, setup):

        self.lp = Login(self.driver)

        self.lp.doLogin(self.Email, self.Password)

        self.addCust = addCustomer(self.driver)

        self.addCust.clickCustomers()

        self.addCust.clickCustomersMenu()

        self.search = searchCustomer(self.driver)

        self.search.setEmail(self.searchEmail)

        self.search.clickSearch()

        getEmail = self.search.searchByEmail(self.searchEmail)

        assert self.searchEmail == getEmail


