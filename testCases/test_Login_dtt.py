import pytest
from pageObjects.test_LoginPage import test_LoginPage
from selenium import webdriver
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtility

class Test_002_DTT_Login:
    baseURL = ReadConfig.getApplicaionURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()
    lst_status = []

    @pytest.mark.regresion
    def test_login(self,setup):
        self.logger.info("************** Verifying Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = test_LoginPage(self.driver)
        self.rows = XLUtility.getrowcount(self.path,"Sheet1")
        print("Number of rows are:", self.rows)


        for r in range(2,self.rows+1):
            self.user = XLUtility.readdata(self.path,'Sheet1',r,1)
            self.passwd = XLUtility.readdata(self.path,'Sheet1',r,2)
            self.exp = XLUtility.readdata(self.path,'Sheet1',r,3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.passwd)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Passed***")
                    self.lp.clickLogout()
                    self.lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****Failed***")
                    self.lp.clickLogout()
                    self.lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Failed***")
                    self.lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****Passed***")
                    self.lst_status.append("Pass")

        if "Fail" not in self.lst_status:
            self.logger.info("*************Login DDT Test Passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Login DDT Test Failed*********")
            self.driver.close()
            assert False
        self.logger.info("*********End of Login DDT Test************")
        self.logger.info("***********Completed Test_002_DTT_Login*********")


'''
            if act_title == "Dashboard / nopCommerce administration":
                assert True
                self.logger.info("************** Login Test is Passed **************")
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.logger.error("************** Login Test is Failed **************")
                self.driver.close()
                assert False
'''
