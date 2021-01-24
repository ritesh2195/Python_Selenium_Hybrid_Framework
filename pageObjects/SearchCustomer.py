from selenium.webdriver.common.by import By

from pageObjects.BasePage import basePage


class searchCustomer(basePage):

    __Email_css = (By.CSS_SELECTOR, "#SearchEmail")

    __FirstName_css = (By.CSS_SELECTOR, "#SearchFirstName")

    __LastName_css = (By.CSS_SELECTOR, "#SearchLastName")

    __buttonSearch_css = (By.CSS_SELECTOR, "#search-customers")

    __searchEmail_xpath = (By.XPATH, "//tr//td[2]")

    __searchName = (By.XPATH, "//tr//td[3]")

    def __init__(self, driver):

        super().__init__(driver)

    def setEmail(self, email):

        self.driver.find_element(*searchCustomer.__Email_css).clear()

        self.driver.find_element(*searchCustomer.__Email_css).send_keys(email)

    def setFirstName(self, firstName):

        self.driver.find_element(*searchCustomer.__FirstName_css).clear()

        self.driver.find_element(*searchCustomer.__FirstName_css).send_keys(firstName)

    def setLastName(self, lastName):

        self.driver.find_element(*searchCustomer.__LastName_css).clear()

        self.driver.find_element(*searchCustomer.__LastName_css).send_keys(lastName)

    def clickSearch(self):

        self.driver.find_element(*searchCustomer.__buttonSearch_css).click()

    def searchByEmail(self, email):

        text = self.driver.find_element(*searchCustomer.__searchEmail_xpath).text

        return text

    def searchByName(self, name):

        text = self.driver.find_element(*searchCustomer.__searchName).text

        return text








