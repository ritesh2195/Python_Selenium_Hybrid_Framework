import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


class addCustomer:
    link_customer_xpath = "//a[@href='#']//span[text()='Customers']"

    link_customer_menu_xpath = "//a[@class='menu-item-link']//span[text()='Customers']"

    Add_new_xpath = "//a[@class='btn bg-blue']"

    Email_box_css = "#Email"

    Password_box_id = "Password"

    FirstName_box_css = "#FirstName"

    LastName_box_css = "#LastName"

    Gender_Male_id = "Gender_Male"

    Gender_Female_id = "Gender_Female"

    DOB_box_id = "DateOfBirth"

    Company_box_id = "Company"

    tax_exempt_click_id = "IsTaxExempt"

    Newsletter_xpath = "//span[text()='Your store name']"

    TestStore2_xpath = "//span[text()='Test store 2']"

    YourStore_xpath = "//span[text()='Your store name']"

    customerRole_xpath = "//span[text()='Registered']"

    Administrator_xpath = "//span[text()='Administrators']"

    Guest_xpath = "//*[text()='Guests']"

    Registered_xpath = "//span[text()='Registered']"

    Vendors_xpath = "//span[text()='Vendors']"

    vendor_box_css = "select[name='VendorId']"

    Active_box_css = "#Active"

    Admin_comment_css = "#AdminComment"

    Save_xpath = "//button[@name='save']"

    def __init__(self, driver):

        self.driver = driver

    def clickCustomers(self):

        self.driver.find_element_by_xpath(self.link_customer_xpath).click()

    def clickCustomersMenu(self):

        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()

    def addNew(self):

        self.driver.find_element_by_xpath(self.Add_new_xpath).click()

    def setEmail(self, email):

        self.driver.find_element_by_css_selector(self.Email_box_css).clear()

        self.driver.find_element_by_css_selector(self.Email_box_css).send_keys(email)

    def setPassword(self, password):

        self.driver.find_element_by_id(self.Password_box_id).clear()

        self.driver.find_element_by_id(self.Password_box_id).send_keys(password)

    def setFirstName(self, FirstName):

        self.driver.find_element_by_css_selector(self.FirstName_box_css).clear()

        self.driver.find_element_by_css_selector(self.FirstName_box_css).send_keys(FirstName)

    def setLastName(self, LastName):

        self.driver.find_element_by_css_selector(self.LastName_box_css).clear()

        self.driver.find_element_by_css_selector(self.LastName_box_css).send_keys(LastName)

    def setDOB(self, dob):

        self.driver.find_element_by_id(self.DOB_box_id).clear()

        self.driver.find_element_by_id(self.DOB_box_id).send_keys(dob)

    def setCompany(self, company):

        self.driver.find_element_by_id(self.Company_box_id).clear()

        self.driver.find_element_by_id(self.Company_box_id).send_keys(company)

    def clickTaxExempt(self):

        self.driver.find_element_by_id(self.tax_exempt_click_id).click()

    def setCustomerRoles(self, role):

        self.driver.find_element_by_xpath(self.customerRole_xpath).click()

        # self.driver.find_element_by_xpath(self.customerRole_xpath).clear()

        time.sleep(3)

        if role == "Registered":

            self.listItem = self.driver.find_element_by_xpath(self.Registered_xpath)

        elif role == "Administrator":

            self.listItem = self.driver.find_element_by_xpath(self.Administrator_xpath)

        elif role == "Guests":

            time.sleep(3)

            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()

            self.listItem = self.driver.find_element_by_xpath(self.Guest_xpath)

        elif role == "Vendors":

            self.listItem = self.driver.find_element_by_xpath(self.Vendors_xpath).click()

        time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManagerVendor(self, value):

        element = self.driver.find_element_by_css_selector(self.vendor_box_css)

        drp = Select(element)

        drp.select_by_visible_text(value)

    def setGender(self, gender):

        if gender == "Male":

            self.driver.find_element_by_id(self.Gender_Male_id).click()

        elif gender == "Female":

            self.driver.find_element_by_id(self.Gender_Female_id).click()

    def setAdminComment(self, comment):

        self.driver.find_element_by_css_selector(self.Admin_comment_css).send_keys(comment)

    def clickSave(self):

        self.driver.find_element_by_xpath(self.Save_xpath).click()

    def verifyAddCustomerTest(self):

        return self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
