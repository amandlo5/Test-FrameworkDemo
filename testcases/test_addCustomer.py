from selenium import webdriver
import pytest
from faker import Faker
from selenium.webdriver.common.by import By

from utilities.customLogger import Loggen
from utilities.readproperties import ReadConfig
from pages.LoginPage import LoginPage
from pages.AddNewCustomer import AddCustomer
import time

class Test_003_Add_Customer:

    baseURL = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = Loggen.loggen()

    @pytest.mark.check
    def test_addNewCustomer(self,setup):
        self.logger.info("***************TC STarted************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.add = AddCustomer(self.driver)
        time.sleep(3)
        self.add.clickCustomerMenu()
        self.add.addNewCustomer()
        faker = Faker()
        email = faker.email()
        password = faker.password()
        fname= faker.first_name()
        lname = faker.last_name()
        self.add.enterEmail(email)
        time.sleep(2)
        self.add.enterPassword(faker.password())
        time.sleep(2)
        self.add.enterFirstName(fname)
        time.sleep(2)
        self.add.enterLastName(lname)
        self.add.selectGender('male')
        self.add.dateOfBirth("3/15/1993")
       # self.add.selectNewsLetter()
        time.sleep(2)
        # self.add.customerRoles('Guests')
        # time.sleep(2)
        self.add.customerRoles('Administrators')
        time.sleep(2)
        self.add.selectVendor('Vendor 2')
        self.add.adminComment("Testing QA")
        self.add.clickSave()
        time.sleep(5)
        self.logger.debug("***********Customer added********************")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*************Customer added successfully************")
        else:
            self.driver.save_screenshot("C:/Users/DELL/PycharmProjects/Test FrameworkDemo/screenshots/failedaddcustomer.png")
            self.logger.debug("**************Failed adding**************")
            assert True == False



