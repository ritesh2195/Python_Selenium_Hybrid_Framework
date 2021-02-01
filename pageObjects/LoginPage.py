from selenium.webdriver.common.by import By

from pageObjects.BasePage import basePage


class Login(basePage):

    __text_Email_css = (By.CSS_SELECTOR, "#Email")

    __text_Password_css = (By.CSS_SELECTOR, "#Password")

    __button_login_xpath = (By.XPATH, "//input[@type='submit']")

    __button_logout_linktext = (By.LINK_TEXT, "Logout")

    __UserName__css = (By.CSS_SELECTOR, ".account-info")

    def __init__(self, driver):

        super().__init__(driver)

    def setEmail(self, email):

        self.driver.find_element(*Login.__text_Email_css).clear()

        self.driver.find_element(*Login.__text_Email_css).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*Login.__text_Password_css).clear()

        self.driver.find_element(*Login.__text_Password_css).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*Login.__button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*Login.__button_logout_linktext).click()

    def doLogin(self, email, password):

        self.driver.find_element(*Login.__text_Email_css).clear()

        self.driver.find_element(*Login.__text_Email_css).send_keys(email)

        self.driver.find_element(*Login.__text_Password_css).clear()

        self.driver.find_element(*Login.__text_Password_css).send_keys(password)

        self.driver.find_element(*Login.__button_login_xpath).click()

    def getTitle(self):

        return self.getPageTitle()

    def getUserName(self):

        return self.driver.find_element(*Login.__UserName__css).text
