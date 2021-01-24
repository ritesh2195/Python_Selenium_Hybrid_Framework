from selenium.webdriver.common.by import By

from pageObjects.BasePage import basePage


class searchCustomer(basePage):

    Email_css = (By.CSS_SELECTOR, "#SearchEmail")

    FirstName_css = (By.CSS_SELECTOR, "#SearchFirstName")

    LastName_css = (By.CSS_SELECTOR, "#SearchLastName")

    buttonSearch_css = (By.CSS_SELECTOR, "#search-customers")

    searchEmail_xpath = (By.XPATH, "//tr//td[2]")

    searchName = (By.XPATH, "//tr//td[3]")

    def __init__(self, driver):

        super().__init__(driver)

    def setEmail(self, email):

        self.driver.find_element(*searchCustomer.Email_css).clear()

        self.driver.find_element(*searchCustomer.Email_css).send_keys(email)

    def setFirstName(self, firstName):

        self.driver.find_element(*searchCustomer.FirstName_css).clear()

        self.driver.find_element(*searchCustomer.FirstName_css).send_keys(firstName)

    def setLastName(self, lastName):

        self.driver.find_element(*searchCustomer.LastName_css).clear()

        self.driver.find_element(*searchCustomer.LastName_css).send_keys(lastName)

    def clickSearch(self):

        self.driver.find_element(*searchCustomer.buttonSearch_css).click()

    def searchByEmail(self, email):

        text = self.driver.find_element(*searchCustomer.searchEmail_xpath).text

        return text

    def searchByName(self, name):

        text = self.driver.find_element(*searchCustomer.searchName).text

        return text








