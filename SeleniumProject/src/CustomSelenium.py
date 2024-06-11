from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomSelenium:

    def __int__(self,driver):
        self.driver = driver
        self.default_timeout = 15

    def wait_and_input(self,locator, text):
        #timeout = timeout if timeout else  self.default_timeout

        WebDriverWait(self.driver).until(
            EC.invisibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self,locator,timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        ).click()