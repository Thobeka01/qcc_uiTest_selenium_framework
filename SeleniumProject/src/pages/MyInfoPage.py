from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumProject.src.helpers.config_helpers import get_base_url


class MyInfoPage:

    def __int__(self, driver):
        self.driver = driver

    def go_to_my_info_page(self):
        Myinfo_url = get_base_url()
        self.driver.get(Myinfo_url)
        self.driver.maximize_window()


    def info_login_username(self, username):
        info_input_locator = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input")  # Initialise Locator
        username_info = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(info_input_locator))
        username_info.send_keys(username)

    def info_login_password(self, password):
        password_info_locator = (By.NAME, "password")  # Initialise Locator
        password_info = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(password_info_locator))
        password_info.send_keys(password)

    def info_login_button(self):
        button_input_locator = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")  # Initialise Locator
        button_info = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_input_locator))
        button_info.click()

    def info_button(self):
        button_my_info_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span")  # Initialise Locator
        button_my_info = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_my_info_locator))
        button_my_info.click()

#editing contact details
    def contact_details (self):
        contact_details_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a")  # Initialise Locator
        button_contact = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(contact_details_locator ))
        button_contact.click()


    def street_input(self, street1):
        street1_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > input")  # Initialise Locator
        street1_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(street1_locator))
        street1_input.send_keys(street1)

    def city_input(self, city):
        city_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(3) > div > div:nth-child(3) > div > div:nth-child(2) > input")  # Initialise Locator
        city_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(city_locator))
        city_input.send_keys(city)

    def state_input(self, state):
        state_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(3) > div > div:nth-child(4) > div > div:nth-child(2) > input")  # Initialise Locator
        state_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(state_locator))
        state_input.send_keys(state)

    def zip_input(self, zip):
        zip_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(3) > div > div:nth-child(5) > div > div:nth-child(2) > input")  # Initialise Locator
        zip_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(zip_locator))
        zip_input.send_keys(zip)

    def mobile_input(self, mobile):
        mobile_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(6) > div > div:nth-child(2) > div > div:nth-child(2) > input")  # Initialise Locator
        mobile_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(mobile_locator))
        mobile_input.send_keys(mobile)

    def save_contact_details(self):
        save_contact_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div.oxd-form-actions > button")  # Initialise Locator
        save_contact = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(save_contact_locator))
        save_contact.click()







