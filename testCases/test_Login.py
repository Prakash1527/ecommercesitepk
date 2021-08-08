import pytest
from pageObjects.test_LoginPage import test_LoginPage
from selenium import webdriver
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicaionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("************** test_homePageTitle *************")
        self.logger.info("************** Verifying Home Page Title ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home page title test is passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Howe page title test is failed **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** Verifying Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = test_LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login Test is Passed **************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************** Login Test is Failed **************")
            self.driver.close()
            assert False

