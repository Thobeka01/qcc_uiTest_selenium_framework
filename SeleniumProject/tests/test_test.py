import pytest
from selenium import webdriver



#opening webbrower with tests
@pytest.mark.usefixtures("init_driver")
class test_test:


   def test_open_broweser(self):
       self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
       #self.default_timeout = 15
       print("browser opened successfully")
