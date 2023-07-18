import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import Loggen
from utilities import ExcelUtils
import time

class Test_002_Login_ddt:

    baseURL = ReadConfig.getUrl()
    path = "C:/Users/DELL/PycharmProjects/Test FrameworkDemo/testdata/LoginData.xlsx"

    logger = Loggen.loggen()

    @pytest.mark.check
    def test_login_ddt(self,setup):
        self.logger.info("*********************Test_002_Login_ddt started*****************")
        self.logger.debug("**********************Tc started***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')
        print(self.rows)
        self.columns = ExcelUtils.getColumnCount(self.path,"Sheet1")
        print(self.columns)
        lst_status = []
        for r in range(2,self.rows+1):
            self.username = ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password = ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.exp = ExcelUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                ExcelUtils.writeData(self.path,'Sheet1',r,4,'Pass')
                self.lp.clickLogout()

            else:
                ExcelUtils.writeData(self.path,'Sheet1',r,4,'Fail')

            self.status = ExcelUtils.readData(self.path,'Sheet1',r,4)

            if self.exp == self.status:
                print('Matching')
                ExcelUtils.writeData(self.path,'Sheet1',r,5,'True')
                assert True
            else:
                print('Not Matched')
                ExcelUtils.writeData(self.path, 'Sheet1', r, 5, 'False')
                assert False





        #         if self.exp == "Pass":
        #             self.logger.info("****Passed****")
        #             self.lp.clickLogout()
        #             lst_status.append("Pass")
        #         elif self.exp == "Fail":
        #             self.logger.info("*****Failed*****")
        #             self.lp.clickLogout()
        #             lst_status.append("Fail")
        #
        #     elif act_title != exp_title:
        #         if self.exp == 'Pass':
        #             self.logger.info("*********Failed**********")
        #             lst_status.append("Fail")
        #         elif self.exp == 'Fail':
        #             self.logger.info("*********Passed********")
        #             lst_status.append("Pass")
        #
        # if "Fail" not in lst_status:
        #     self.driver.close()
        #     assert True
        # else:
        #     self.driver.close()
        #     assert False




