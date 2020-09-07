from pageObjects.SearchCustomer import searchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.AddCustomePage import addCustomer
from pageObjects.LoginPage import Login


class TestSearch_004:

    baseURL = ReadConfig.getApplicationURL()

    Email = ReadConfig.getEmail()

    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchgCustomer(self, setup):

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

        self.search = searchCustomer(self.driver)

        self.search.setEmail("ritesh21@gmail.com")

        self.search.clickSearch()

        status = self.search.searchByEmail("ritesh21@gmail.com")

        assert True == status