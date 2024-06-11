from selenium import webdriver
import pytest
import os

#setting up the webdriver
@pytest.fixture(scope='class')
def init_driver(request):


    supported_browser = ['chrome','ch','headlesschrome','firefox','ff']


    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise  Exception("The environment variable 'BROWSER' must be set ")

    browser = browser.lower()
    if browser not in supported_browser:
        raise Exception(f"Provided browser '{browser} is no one of the supported browsers.'"
                        f"Supported are: {supported_browser}")


    if browser in  ('chrome','ch') :
        driver = webdriver.Chrome()
    elif browser in ('firefox','ff'):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()

