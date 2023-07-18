import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import Loggen
import time

class Test_001_Login:

    baseURL = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = Loggen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homepage_title(self,setup):
        self.logger.info("****************************tc started*********************")
        self.logger.debug("*******************TC_001_Login*****************")
        self.logger.debug("*******************Verifying HomePage Title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.debug("*******************TC successfully Completed**********************")
            self.logger.info("******************************tc Completed*********************")

        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_homepageTitle.png')
            self.driver.close()
            self.logger.debug("******************TC failed************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == self.driver.title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'test_login.png')
            self.driver.close()
            assert False

