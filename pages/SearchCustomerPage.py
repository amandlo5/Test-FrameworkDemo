class SearchCustomer:

    email_id= "SearchEmail"
    fname_id = "SearchFirstName"
    lname_id = "SearchLastName"
    search_btn_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element('id',self.email_id).clear()
        self.driver.find_element('id', self.email_id).send_keys(email)

    def setFname(self,fname):
        self.driver.find_element('id',self.fname_id).clear()
        self.driver.find_element('id', self.fname_id).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element("id",self.lname_id).clear()
        self.driver.find_element("id", self.lname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element('id',self.search_btn_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements('xpath',self.table_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements('xpath',self.table_columns_xpath))

    def searchByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element('xpath',self.table_xpath)
            emailId = table.find_element('xpath',"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]")
            if emailId == email:
                flag = True
                break
        return flag

    def searchByName(self,Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element('xpath',self.table_xpath)
            name = table.find_element('xpath',"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]")
            if name == Name:
                flag = True
                break
        return flag
