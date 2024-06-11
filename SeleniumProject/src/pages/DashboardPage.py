from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumProject.src.helpers.config_helpers import get_base_url


class DashboardPage:

    def __int__(self, driver):
        self.driver = driver

    def go_to_my_info_page(self):
        dashboard_url = get_base_url()
        self.driver.get(dashboard_url)
        self.driver.maximize_window()

    def click_dashboard(self):
        click_dashboard_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a")  # Initialise Locator
        dashboard1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(click_dashboard_locator))
        dashboard1.click()


    def click_time_at_work(self):
        click_time_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button")  # Initialise Locator
        time_btn1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(click_time_locator ))
        time_btn1.click()


    #my actions
    def click_my_actions_1(self):
        click_actions_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/button")  # Initialise Locator
        action1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(click_actions_locator))
        action1.click()

    def click_my_actions_2(self):
        click_actions2_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(2) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(2) > p")  # Initialise Locator
        action2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(click_actions2_locator))
        action2.click()


    #quick luanch
    def quick_launch1(self):
        launch1_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(1) > button > svg")  # Initialise Locator
        launch1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(launch1_locator))
        launch1.click()

    def quick_launch2(self):
        launch2_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(2) > button > svg")  # Initialise Locator
        launch2 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(launch2_locator))
        launch2.click()

    def quick_launch3(self):
        launch3_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(3) > button > svg")  # Initialise Locator
        launch3 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(launch3_locator))
        launch3.click()

    def quick_launch4(self):
        launch4_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(4) > button > svg")  # Initialise Locator
        launch4 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(launch4_locator))
        launch4.click()

    def quick_launch5(self):
        launch5_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(5) > button > svg")  # Initialise Locator
        launch5 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(launch5_locator))
        launch5.click()

    def quick_launch6(self):
        launch6_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(3) > div > div.orangehrm-dashboard-widget-body > div > div:nth-child(6) > button > svg")  # Initialise Locator
        launch6 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(launch6_locator))
        launch6.click()


    #Buzz latest pag
    def buzz_page(self):
        buzz_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/div")  # Initialise Locator
        buzz1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(buzz_locator))
        buzz1.click()

    def pie_chart(self):
        pie_chart_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[7]/div/div[2]/div/div/canvas")  # Initialise Locator
        pie_chart = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(pie_chart_locator))
        pie_chart.click()