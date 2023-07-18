import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    customer_link_xpath = "//nav[@class='mt-2']/ul/li[4]/ul/li/a/i"
    addnew_xpath = "//a[@class='btn btn-primary']/i"
    email_id = 'Email'
    password_id = 'Password'
    fname_name = 'FirstName'
    lname_name = 'LastName'
    male_id = 'Gender_Male'
    female_id = 'Gender_Female'
    dob_id = 'DateOfBirth'
    newletter_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover']"
    test_store_2_xpath = "//div[@class='k-list-scroller']/ul/li[2]"
    registered_deselect_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']/ul/li/span"
    customer_roles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    admninistrators_xpath = "//li[contains(text(),'Administrators')]"
    forum_xpath = "//li[contains(text(),'Forum Moderators')]"
    guests_xpath = "//li[contains(text(),'Guests')]"
    registered_xpath = "//li[contains(text(),'Guests')]"
    vendors_xpath = "//li[contains(text(),'Vendors')]"
    manager_vendor_id = "VendorId"
    admin_comment_id = "AdminComment"
    save_xpath = "//button[@type='submit' and @name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickCustomerMenu(self):
        self.driver.find_element('xpath',self.customer_xpath).click()
        self.driver.find_element('xpath',self.customer_link_xpath).click()

    def addNewCustomer(self):
        self.driver.find_element('xpath',self.addnew_xpath).click()

    def enterEmail(self,email):
        self.driver.find_element("id",self.email_id).send_keys(email)

    def enterPassword(self,password):
        self.driver.find_element("id",self.password_id).send_keys(password)

    def enterFirstName(self,fname):
        self.driver.find_element("name",self.fname_name).send_keys(fname)

    def enterLastName(self,lname):
        self.driver.find_element("name",self.lname_name).send_keys(lname)

    def selectGender(self,gender):
        if gender == 'male':
            self.driver.find_element("id",self.male_id).click()
        else:
            self.driver.find_element("id",self.female_id).click()

    def dateOfBirth(self,dob):
        self.driver.find_element("id",self.dob_id).send_keys(dob)

    def selectNewsLetter(self):
        self.driver.find_element('xpath',self.newletter_xpath).click()
        self.driver.find_element('xpath',self.test_store_2_xpath).click()


    def customerRoles(self,role):
        self.driver.find_element('xpath', self.registered_deselect_xpath).click()
        self.driver.find_element('xpath',self.customer_roles_xpath).click()
        if role == 'Registered':
            self.listitem = self.driver.find_element('xpath',self.registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element('xpath', self.admninistrators_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element('xpath', self.forum_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element('xpath', self.guests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element('xpath', self.vendors_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)


    def selectVendor(self,value):
        drp = Select(self.driver.find_element('id',self.manager_vendor_id))
        drp.select_by_visible_text(value)

    def adminComment(self,comment):
        self.driver.find_element('id',self.admin_comment_id).send_keys(comment)

    def clickSave(self):
        self.driver.find_element('xpath',self.save_xpath).click()