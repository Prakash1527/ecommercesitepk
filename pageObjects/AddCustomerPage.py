import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add Customer Page
    #lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customer')]"
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitems_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    #lnkCustomers_menuitems_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdGendermale_xpath = "//input[@id='Gender_Male']"
    rdGenderfemail_xpath = "//input[@id='Gender_Female']"
    txtdob_xpath = "//input[@id='DateOfBirth']"
    txtCompany_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "// li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "// li[contains(text(), 'Registered')]"
    lstitemGuests_xpath = "// li[contains(text(), 'Guests')]"
    lstitemVendors_xpath = "// li[contains(text(), 'Vendors')]"
    lstitemFM_xpath = "// li[contains(text(), 'Forum Moderators')]"
    drpmgrofVendor_xpath = "//select[@id='VendorId']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitems_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,passwrd):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(passwrd)

    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lastname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == "Guests":
            # Here user can be registered or guests, only one
            self.driver.find_element_by_xpath('//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(5)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVendor(self,value):
        drpdwn = Select(self.driver.find_element_by_xpath(self.drpmgrofVendor_xpath))
        drpdwn.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.rdGendermale_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.rdGenderfemail_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdGendermale_xpath).click()
    def setdob(self,dob):
        self.driver.find_element_by_xpath(self.txtdob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompany_xpath).send_keys(comname)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()