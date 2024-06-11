from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumProject.src.helpers.config_helpers import get_base_url


class Buzzpage:

    def __int__(self, driver):
        self.driver = driver

    def go_to_my_info_page(self):
        blog_url = get_base_url()
        self.driver.get(blog_url)
        self.driver.maximize_window()

    def click_buzz_page(self):
        buzz_page_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a")  # Initialise Locator
        buzz2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(buzz_page_locator))
        buzz2.click()

    def insert_commment(self,inputcomment):
        comment_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div > div.oxd-sheet.oxd-sheet--rounded.oxd-sheet--gutters.oxd-sheet--white.orangehrm-buzz-create-post > div.orangehrm-buzz-create-post-header > div.orangehrm-buzz-create-post-header-text > form > div > textarea")  # Initialise Locator
        comment = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(comment_locator))
        comment.send_keys(inputcomment)

    def post_button(self):
        post_button_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/div/button")  # Initialise Locator
        post = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(post_button_locator))
        post.click()

    def like_post(self):
        like_locator = (By.CSS_SELECTOR,"#heart-svg")  # Initialise Locator
        like = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(like_locator))
        like.click()

    def share_post(self):
        share_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div > div.oxd-grid-1.orangehrm-buzz-newsfeed-posts > div:nth-child(3) > div > div.orangehrm-buzz-post-footer > div.orangehrm-buzz-post-actions > button:nth-child(3)")  # Initialise Locator
        share = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(share_locator))
        share.click()

    def share_button(self):
        share_button_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > form > div.oxd-form-actions.orangehrm-buzz-post-modal-actions > button")  # Initialise Locator
        share1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(share_button_locator))
        share1.click()

    def three_dots(self):
        three_dots_locator = (By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li")  # Initialise Locator
        share2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(three_dots_locator))
        share2.click()

    def edit_button(self):
        edit_button_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div > div.oxd-grid-1.orangehrm-buzz-newsfeed-posts > div:nth-child(1) > div > div.orangehrm-buzz-post > div > div.orangehrm-buzz-post-header-config > li > ul > li:nth-child(2) > p")  # Initialise Locator
        share3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(edit_button_locator))
        share3.click()

    def edit_post(self,edit):
        share_button_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > form > div.orangehrm-buzz-post-modal-header > div.orangehrm-buzz-post-modal-header-text > div > textarea")  # Initialise Locator
        share4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(share_button_locator))
        share4.send_keys(edit)

    def edit_post_button(self):
        share_button_locator = (By.XPATH,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > form > div.oxd-form-actions.orangehrm-buzz-post-modal-actions > button")  # Initialise Locator
        share5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(share_button_locator))
        share5.click()

    def delete_button1(self):
        delete_button_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/ul/li[1]/p")  # Initialise Locator
        share6 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(delete_button_locator))
        share6.click()

    def delete_button2(self):
        delete2_button_locator = (By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]")  # Initialise Locator
        share7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(delete2_button_locator))
        share7.click()

    def share_image(self):
        share_image_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/button[2]/span")  # Initialise Locator
        share_image= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located( share_image_locator))
        share_image.click()

    def most_commented_posts(self):
        most_commented_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div:nth-child(1) > div > div.orangehrm-post-filters > button:nth-child(3)")  # Initialise Locator
        most_commented = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(most_commented_locator))
        most_commented.click()


    def add_image(self):
        add_image_locator= (By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/button[2]")  # Initialise Locator
        add_image = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(add_image_locator))
        add_image.click()

    def post_image(self):
        post_image_locator = (By.CSS_SELECTOR, "#Buzz\ Newsfeed > div > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > form > div.oxd-form-actions.orangehrm-buzz-post-modal-actions > button")  # Initialise Locator
        post_image = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(post_image_locator))
        post_image.click()