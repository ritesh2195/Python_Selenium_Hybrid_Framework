import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.BasePage import basePage


class addCustomer(basePage):

    __link_customer_xpath = (By.XPATH, "//a[@href='#']//span[text()='Customers']")

    __link_customer_menu_xpath = (By.XPATH, "//a[@class='menu-item-link']//span[text()='Customers']")

    __Add_new_xpath = (By.XPATH, "//a[@class='btn bg-blue']")

    __Email_box_css = (By.CSS_SELECTOR, "#Email")

    __Password_box_id = (By.ID, "Password")

    __FirstName_box_css = (By.CSS_SELECTOR, "#FirstName")

    __LastName_box_css = (By.CSS_SELECTOR, "#LastName")

    __Gender_Male_id = (By.ID, "Gender_Male")

    __Gender_Female_id = (By.ID, "Gender_Female")

    __DOB_box_id = (By.ID, "DateOfBirth")

    __Company_box_id = (By.ID, "Company")

    __tax_exempt_click_id = (By.ID, "IsTaxExempt")

    __Newsletter_xpath = (By.XPATH, "//span[text()='Your store name']")

    __TestStore2_xpath = (By.XPATH, "//span[text()='Test store 2']")

    __YourStore_xpath = (By.XPATH, "//span[text()='Your store name']")

    __customerRole_xpath = (By.XPATH, "//span[text()='Registered']")

    __Administrator_xpath = (By.XPATH, "//span[text()='Administrators']")

    __Guest_xpath = (By.XPATH, "//*[text()='Guests']")

    __Registered_xpath = (By.XPATH, "//span[text()='Registered']")

    __Vendors_xpath = (By.XPATH, "//span[text()='Vendors']")

    __vendor_box_css = (By.CSS_SELECTOR, "select[name='VendorId']")

    __Active_box_css = (By.CSS_SELECTOR, "#Active")

    __Admin_comment_css = (By.CSS_SELECTOR, "#AdminComment")

    __Save_xpath = (By.XPATH, "//button[@name='save']")

    __SuccessMessage_xpath = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")

    def __init__(self, driver):

        super().__init__(driver)

    def clickCustomers(self):

        self.driver.find_element(*addCustomer.__link_customer_xpath).click()

    def clickCustomersMenu(self):

        self.elementToClickable(self.__link_customer_menu_xpath)

        self.driver.find_element(*addCustomer.__link_customer_menu_xpath).click()

    def addNew(self):

        self.driver.find_element(*addCustomer.__Add_new_xpath).click()

    def setEmail(self, email):

        self.driver.find_element(*addCustomer.__Email_box_css).clear()

        self.driver.find_element(*addCustomer.__Email_box_css).send_keys(email)

    def setPassword(self, password):

        self.driver.find_element(*addCustomer.__Password_box_id).clear()

        self.driver.find_element(*addCustomer.__Password_box_id).send_keys(password)

    def setFirstName(self, FirstName):

        self.driver.find_element(*addCustomer.__FirstName_box_css).clear()

        self.driver.find_element(*addCustomer.__FirstName_box_css).send_keys(FirstName)

    def setLastName(self, LastName):

        self.driver.find_element(*addCustomer.__LastName_box_css).clear()

        self.driver.find_element(*addCustomer.__LastName_box_css).send_keys(LastName)

    def setDOB(self, dob):

        self.driver.find_element(*addCustomer.__DOB_box_id).clear()

        self.driver.find_element(*addCustomer.__DOB_box_id).send_keys(dob)

    def setCompany(self, company):

        self.driver.find_element(*addCustomer.__Company_box_id).clear()

        self.driver.find_element(*addCustomer.__Company_box_id).send_keys(company)

    def clickTaxExempt(self):

        self.driver.find_element(*addCustomer.__tax_exempt_click_id).click()

    def setCustomerRoles(self, role):

        self.driver.find_element(*addCustomer.__customerRole_xpath).click()

        if role == "Registered":

            self.elementToClickable(self.__Registered_xpath)

            self.listItem = self.driver.find_element(*addCustomer.__Registered_xpath)

        elif role == "Administrator":

            self.elementToClickable(self.__Administrator_xpath)

            self.listItem = self.driver.find_element(*addCustomer.__Administrator_xpath)

        elif role == "Guests":

            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()

            self.listItem = self.driver.find_element(*addCustomer.__Guest_xpath)

        elif role == "Vendors":

            self.listItem = self.driver.find_element(*addCustomer.__Vendors_xpath)

        self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManagerVendor(self, value):

        element = self.driver.find_element(*addCustomer.__vendor_box_css)

        drp = Select(element)

        drp.select_by_visible_text(value)

    def setGender(self, gender):

        if gender == "Male":

            self.driver.find_element(*addCustomer.__Gender_Male_id).click()

        elif gender == "Female":

            self.driver.find_element(*addCustomer.__Gender_Female_id).click()

    def setAdminComment(self, comment):

        self.driver.find_element(*addCustomer.__Admin_comment_css).send_keys(comment)

    def clickSave(self):

        self.driver.find_element(*addCustomer.__Save_xpath).click()

    def verifyAddCustomerTest(self):

        return self.driver.find_element(*addCustomer.__SuccessMessage_xpath).text


