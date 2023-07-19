from selenium import webdriver
import pytest
from faker import Faker
from selenium.webdriver.common.by import By

from utilities.customLogger import Loggen
from utilities.readproperties import ReadConfig
from pages.LoginPage import LoginPage
from pages.AddNewCustomer import AddCustomer
from pages.SearchCustomerPage import SearchCustomer
import time


class Test_004_Search:
    baseURL = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = Loggen.loggen()

    @pytest.mark.sanity
    def test_searchByEmail(self, setup):
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
        time.sleep(3)
        self.search = SearchCustomer(self.driver)
        self.search.setEmail("joyce77@example.net")
        self.search.clickSearch()
        time.sleep(3)
        status = self.search.searchByEmail("joyce77@example.net")
        assert True != status
        self.logger.debug("********************TC Completed*****************")

    @pytest.mark.sanity
    def test_SearchByName(self,setup):
        self.logger.info("********************Search Customer By Name****************")
        self.logger.debug("*********************TC Started***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.add = AddCustomer(self.driver)
        self.add.clickCustomerMenu()
        self.search = SearchCustomer(self.driver)
        time.sleep(3)
        self.search.setFname("ram")
        self.search.setLname("kumar")
        self.search.clickSearch()
        time.sleep(3)
        status = self.search.searchByName("ram kumar")
        assert True == status

    def test_method(self):
        print('test merge')
    def test_method1(self):
        print("sdet test merge")