import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import ClassVar
from pageObjects.test_LoginPage import test_LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicaionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*************Test_003_AddCustomer*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = test_LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        self.logger.info("****************Login Successfull***************")

        self.logger.info("*****************Starting Add Customer Test**************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("****************Providing Customer Info************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Victor")
        self.addcust.setLastname("Paulson")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setdob("07/05/2021") #Format DD/MM/YYYY
        self.addcust.setCompanyName("BusyQA")
        self.addcust.clickOnSave()

        self.logger.info("********Saviung Customer Info*******")

        self.logger.info("************Add Customer validation started************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        #print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True
            self.logger.info("************Add Customer Test Passed************")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addCustomer_scr.png") # Screenshot
            self.logger.error("***********Add Customer Test Failed*************")
            assert False
        self.driver.close()
        self.logger.info("**************Ending Add Customer Test***************")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


