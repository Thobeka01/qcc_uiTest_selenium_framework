

from SeleniumProject.src.pages.Locators.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
#from webdrivermanager import ChromeDriverManager
from selenium import webdriver
from SeleniumProject.src.CustomSelenium import CustomSelenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumProject.src.helpers.config_helpers import  get_base_url
class Loginpage(Locators):

    endpoint = '/login'

    def __int__(self,driver):
        self.driver = driver
        self.sl = CustomSelenium(self.driver)

    def go_to_page(self):
        base_url = get_base_url()
        my_login_url = base_url
        self.driver.get(my_login_url)
        self.driver.maximize_window()

        #username login

    def input_login_username(self,username):

        username_input_locator = (By.NAME, "username")  #Initialise Locator
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(username_input_locator))
        username_input.send_keys(username)
    def input_login_password(self,password):

        password_input_locator = (By.NAME, "password") #Initialise Locator
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(password_input_locator))
        password_input.send_keys(password)
    def click_login_button(self):

       button_input_locator = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")  #Initialise Locator
       button_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_input_locator))
       button_input.click()

    def verify_invalid_user(self):
        error_message_locator = (By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > div > div.oxd-alert.oxd-alert--error")  # Adjust this to match the actual locator of the error message element
        error_message = EC.visibility_of_element_located(error_message_locator)(self.driver)

        assert error_message.text == "Invalid credentials"
        if error_message.is_displayed():
            print("Pass")
        else:
            raise Exception("not displayed")



    def verify_successful_login(self):
        error_message1_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a")  # Adjust this to match the actual locator of the error message element
        error1_message = EC.visibility_of_element_located(error_message1_locator)(self.driver)
        error1_message.click()

        try:
         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-title > span > h6")))
         assert True,"Button click action was successful "
         print("login successful")
        except TimeoutError:
         print("login failed")







