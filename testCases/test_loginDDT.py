import time

import pytest
from pageObjects.LoginPage import Login
from testCases.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.dataProvider import getData


class Test_002_loginDDT(BaseClass):
    logger = LogGen.loggen()

    @pytest.mark.parametrize("email, password", getData())
    def test_login(self, email, password):

        self.logger.info("*********Login Test Test_002 Started***********")

        self.logger.info("********Verifying Logim Function***********")

        self.lp = Login(self.driver)

        self.lp.doLogin(email, password)

        actualTitle = self.lp.getTitle()

        userName = self.lp.getUserName()

        expTitle = "Dashboard / nopCommerce administration"

        assert actualTitle == expTitle

        assert userName == 'John Smith'

        self.logger.info("Login Test is passed")


