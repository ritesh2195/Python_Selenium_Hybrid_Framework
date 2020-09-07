import random
import string

from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.AddCustomePage import addCustomer


class Test_003_addCustomer:
    baseURL = ReadConfig.getApplicationURL()

    Email = ReadConfig.getEmail()

    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addingCustomer(self, setup):
        self.driver = setup

        self.driver.maximize_window()

        self.driver.get(self.baseURL)

        self.driver.implicitly_wait(10)

        self.lp = Login(self.driver)

        self.lp.setEmail(self.Email)

        self.lp.setPassword(self.Password)

        self.lp.clickLogin()

        self.addCust = addCustomer(self.driver)

        self.addCust.clickCustomers()

        self.addCust.clickCustomersMenu()

        self.addCust.addNew()

        # self.email = random_generator() + "@gmail.com"

        self.addCust.setEmail("vdbsbjlkbjb@gmail.com")

        self.addCust.setPassword("vgysyhghc12")

        self.addCust.setFirstName("bshbsbwjbj")

        self.addCust.setLastName("dbhbshbhsb")

        self.addCust.setGender("Male")

        self.addCust.setDOB("9/21/1995")

        self.addCust.setCompany("ritesh")

        self.addCust.clickTaxExempt()

        self.addCust.setCustomerRoles("Registered")

        self.addCust.setManagerVendor("Vendor 1")

        self.addCust.setAdminComment("jbdjnjdbc jbjdnkndf")

        self.addCust.clickSave()

        self.msg=self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text

        if "The new customer has been added successfully.1" in self.msg:

            assert True

        else:

            self.driver.save_screenshot(".\\Screenshots\\"+"test_AddCustomer.png")

            assert True ==False

        self.driver.close()
#def random_generator(size=8, chars=string.ascii_lowercase + string.digits()):
#    return ''.join(random.choice(chars) for x in range(size))
