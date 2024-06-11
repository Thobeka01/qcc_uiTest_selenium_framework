from selenium import webdriver
from SeleniumProject.tests.test_test import test_test
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumProject.src.pages.Loginpage import Loginpage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import pytest

@pytest.mark.usefixtures("init_driver")
class TestLoginTestCases:
    #LOGIN_USERNAME = (By.NAME, "username")
    #driver = webdriver.Chrome()
    @pytest.mark.smoke
    def test_invalid_login_details(self):

        Loginpage.go_to_page(self)
        time.sleep(3)
        #test_test.test_open_broweser(self,driver)
        #time.sleep(3)
        # self.default_timeout = 10
        Loginpage.input_login_username(self, "yvfufctf")
        time.sleep(2)
        Loginpage.input_login_password(self, "admin1234")
        time.sleep(2)
        Loginpage.click_login_button(self)
        time.sleep(10)
        Loginpage.verify_invalid_user(self)
        time.sleep(2)

    @pytest.mark.smoke
    def test_login_existing_user(self):

        #Loginpage.go_to_page(self)
        #time.sleep(3)
        #test_test.test_open_broweser(self)
        #self.default_timeout = 10
        Loginpage.input_login_username(self,"Admin")
        time.sleep(2)
        Loginpage.input_login_password(self, "admin123")
        time.sleep(2)
        Loginpage.click_login_button(self)
        time.sleep(10)
        Loginpage.verify_successful_login(self)
        time.sleep(2)

        #self.driver.quit()