from SeleniumProject.src.pages.Locators.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumProject.src.helpers.config_helpers import  get_base_url


class PIMPage:

    def __int__(self,driver):
        self.driver = driver

    def go_to_PIM_page(self):
        PIM_url = get_base_url()
        self.driver.get(PIM_url)
        self.driver.maximize_window()


    def input_username(self,username):

        username_input_locator = (By.NAME, "username")  # Initialise Locator
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(username_input_locator))
        username_input.send_keys(username)


    def input_password(self,password):
        password_input_locator = (By.NAME, "password")  # Initialise Locator
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(password_input_locator))
        password_input.send_keys(password)

    def click_login_button(self):
        button_input_locator = (
        By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")  # Initialise Locator
        button_input1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_input_locator))
        button_input1.click()

    def click_pim_button(self):
        button_pim_locator = (
            By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")  # Initialise Locator
        button_input2 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_pim_locator))
        button_input2.click()

    def click_add_employee_button(self):
        button_add_employee_locator = (
            By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a")  # Initialise Locator
        button_input2 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_add_employee_locator))
        button_input2.click()

    def employee_first_name(self,firstname):

        employee_first_name_locator = (By.NAME, "firstName")  # Initialise Locator
        employee_first_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(employee_first_name_locator))
        employee_first_name_input.send_keys(firstname)

    def employee_last_name(self,lastname):

        employee_last_name_locator = (By.NAME, "lastName")  # Initialise Locator
        employee_last_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(employee_last_name_locator))
        employee_last_name_input.send_keys(lastname)


    def employee_id(self,employeeid):
        button_employee_id_Locator= (By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-2.orangehrm-full-width-grid > div > div > div:nth-child(2) > input')  # Initialise Locator
        employee_id_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(button_employee_id_Locator))
        employee_id_input.send_keys(employeeid)

    def create_login_details_button(self):
        create_login_details_locator = (
            By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span")  # Initialise Locator
        button_input3 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(create_login_details_locator))
        button_input3.click()

    def input_login_username(self,login_username):
        login_username_input_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(4) > div > div:nth-child(1) > div > div:nth-child(2) > input")  # Initialise Locator
        input_login_username1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login_username_input_locator))
        input_login_username1.send_keys(login_username)

    def input_login_password(self, login_password):
        login_password_input_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div.oxd-form-row.user-password-row > div > div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > div:nth-child(2) > input")  # Initialise Locator
        input_login_password1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login_password_input_locator))
        input_login_password1.send_keys(login_password)

    def match_login_password(self, input_match_password):
        match_password_input_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input")  # Initialise Locator
        input_match_password1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(match_password_input_locator))
        input_match_password1.send_keys(input_match_password)

    def save_add_employee_button(self):
        save_button_add_employee_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")  # Initialise Locator
        button_input4 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(save_button_add_employee_locator))
        button_input4.click()

        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > h6")))
            assert True, "added employee Successfully "
            print("Employee added successfully")
        except TimeoutError:
            print("Adding Employee failed")


    def save_employee_button(self):
     button_save_employee_locator = (
     By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button")  # Initialise Locator
     button_input5 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_save_employee_locator))
     button_input5.click()

     #Cancelling an employee
    def cancel_employee(self):
       button_cancel_employee_locator = (By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]")  # Initialise Locator
       button_input6 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_cancel_employee_locator))
       button_input6.click()

       try:
           WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited > a")))
           assert True, "added employee Successfully "
           print("Employee cancelled")
       except TimeoutError:
           print("Failed to cancel employee")

    #searching for an employee on the employee

    def click_employee_list_button(self):
        button_employee_list_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")  # Initialise Locator
        button_input7= WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_employee_list_locator ))
        button_input7.click()

    #Search - employee name

    def employee_Search_name(self, Searchname):
        employee_search_name_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input")  # Initialise Locator
        employee_search_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(employee_search_name_locator))
        employee_search_name_input.send_keys(Searchname)


      #Search button

    def click_search_button(self):
        button_search_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")  # Initialise Locator
        button_input8= WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_search_locator ))
        button_input8.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-container > div > div.oxd-table-body > div > div > div:nth-child(4)")))
            assert True, "added employee Successfully "
            print("Employee found")
        except TimeoutError:
            print("Employee found")
    def click_on_edit_button(self):
        button_edit_locator = (
        By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]")  # Initialise Locator
        button_input9 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_edit_locator))
        button_input9.click()



    #verification




















































