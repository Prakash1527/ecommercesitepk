import pytest
import time
from pageObjects.test_LoginPage import test_LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicaionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerbyName(self,setup: WebDriver):
        self.logger.info("*************Search Customer by Name*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = test_LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.logger.info("****************Login Successfull***************")

        self.logger.info("**************Starting search customer by name***********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*******************searching customer by name************")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName("Terces")
        self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerbyName("Victoria Terces")
        assert True == status
        self.driver.close()
        self.logger.info("**********************End of Test_SearchCustomerByName_005************")