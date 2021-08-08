from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class SearchCustomer:
    #Add Customer Page for searching
    txtEmail_Id = "SearchEmail"
    txtFirstName = "SearchFirstName"
    txtLastName = "SearchLastName"
    btnSearchCustomer = "search-customers"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"



    def __init__(self, driver: WebDriver):
        self.driver = driver

    def setEmail(self, Email):
        self.driver.find_element_by_id(self.txtEmail_Id).clear()
        self.driver.find_element_by_id(self.txtEmail_Id).send_keys(Email)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName).clear()
        self.driver.find_element_by_id(self.txtFirstName).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName).clear()
        self.driver.find_element_by_id(self.txtLastName).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearchCustomer).click()

    def getNoofRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerbyEmail(self, Email):
        flag = False
        for r in range(1,self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == Email:
                flag = True
                break
        return flag

    def searchCustomerbyName(self, Name):
        flag = False
        for r in range(1,self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
