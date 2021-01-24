from utilities.RandomDataGenerator import *
from pageObjects.LoginPage import Login
from testCases.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.AddCustomePage import addCustomer


class Test_003_addCustomer(BaseClass):
    baseURL = ReadConfig.getApplicationURL()

    Email = ReadConfig.getEmail()

    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addingCustomer(self, setup):

        self.lp = Login(self.driver)

        self.lp.doLogin(self.Email, self.Password)

        self.addCust = addCustomer(self.driver)

        self.addCust.clickCustomers()

        self.addCust.clickCustomersMenu()

        self.addCust.addNew()

        self.addCust.setEmail(email())

        self.addCust.setPassword(password())

        self.addCust.setFirstName(firstName())

        self.addCust.setLastName(lastName())

        self.addCust.setGender("Male")

        self.addCust.setDOB("9/21/1995")

        self.addCust.setCompany(company())

        self.addCust.clickTaxExempt()

        self.addCust.setCustomerRoles("Registered")

        self.addCust.setManagerVendor("Vendor 1")

        self.addCust.setAdminComment(adminComment())

        self.addCust.clickSave()

        self.msg = self.addCust.verifyAddCustomerTest()

        if "The new customer has been added successfully." in self.msg:

            assert True

        else:

            self.captureScreenshot()

            assert True == False
