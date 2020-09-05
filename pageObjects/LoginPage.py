class Login:
    text_Email_css = "#Email"
    text_Password_css = "#Password"
    button_login_xpath = "//input[@type='submit']"
    button_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_css_selector(self.text_Email_css).clear()
        self.driver.find_element_by_css_selector(self.text_Email_css).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_css_selector(self.text_Password_css).clear()
        self.driver.find_element_by_css_selector(self.text_Password_css).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()


