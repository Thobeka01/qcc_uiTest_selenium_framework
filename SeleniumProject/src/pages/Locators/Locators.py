from selenium.webdriver.common.by import By

class Locators:

    LOGIN_USERNAME= (By.NAME,"username")
    lOGIN_PASSWORD = (By.NAME,"username")
    lOGIN_BTN = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")
