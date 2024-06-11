from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumProject.src.helpers.config_helpers import  get_base_url


class Adminpage:

    def __int__(self,driver):
        self.driver = driver

    def go_to_PIM_page(self):
        Admin_url = get_base_url()
        self.driver.get(Admin_url)
        self.driver.maximize_window()

#Click admin page button
    def click_admin_button(self):
        button_admin_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")  # Initialise Locator
        button_admin= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable( button_admin_locator))
        button_admin.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-title > span > h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")))
            assert True, "added employee Successfully "
            print("Admin page opened successfully")
        except TimeoutError:
            print("Admin page failed to open")

    def input_username(self,username):
        employee_username_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.oxd-table-filter > div.oxd-table-filter-area > form > div.oxd-form-row > div > div:nth-child(1) > div > div:nth-child(2) > input")  # Initialise Locator
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(employee_username_locator ))
        username_input.send_keys(username)

    def click_search_button(self):
        button_search_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")  # Initialise Locator
        button_search = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(button_search_locator))
        button_search.click()

    def click_job_button(self):
        button_job_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span")  # Initialise Locator
        button_job= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable( button_job_locator ))
        button_job.click()


    def click_option(self):
        option_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a")  # In
        button_job1= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(option_locator ))
        button_job1.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div.orangehrm-container > div > div.oxd-table-header > div > div:nth-child(2)")))
            print("Job page opened successfully")
        except TimeoutError:
            print("Jop page failed to open ")

      #employemnt status add button
    def click_add_button(self):
        add_button_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button")  # I
        button_add1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(add_button_locator))
        button_add1.click()

    def employment_status_name(self,emplname):
        empl_name_locator=(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-row > div > div:nth-child(2) > input")  # I
        button_add2= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(empl_name_locator))
        button_add2.send_keys(emplname)

    def emp_save_button(self):
        employment_save_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")  # Initialize locator
        employment_save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(employment_save_locator))
        employment_save_button.click()

    #delete employment status
    def delete_checkbox(self):
        employment_delete_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div.orangehrm-container > div > div.oxd-table-body > div:nth-child(7) > div > div:nth-child(1) > div > div > label > span")  # Initialize locator
        employment_delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(employment_delete_locator))
        employment_delete_button.click()

    def delete_selected_message(self):
        delete_selected_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div:nth-child(2) > div > div > button")  # Initialize locator
        delete_selected_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(delete_selected_locator))
        delete_selected_button.click()

    def delete_button_popup(self):
        popup_button_locator = (By.CSS_SELECTOR, "#app > div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > div.orangehrm-modal-footer > button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin")  # Initialize locator
        popup_delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(popup_button_locator))
        popup_delete_button.click()

    def click_organization_checkbox(self):
        button_org_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")  # Init
        button_org = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button_org_locator))
        button_org.click()

    def click_option_org(self):
        option_org_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a")  # In
        button_org1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(option_org_locator ))
        button_org1.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div.oxd-grid-item.oxd-grid-item--gutters.organization-name-container > div > div.oxd-input-group__label-wrapper > label")))
            assert True, "Open job page"
            print("organization opened successfully")
        except TimeoutError:
            print("organization failed to open ")

    def edit_general_info(self):
        edit_info_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div > label > span")
        button_org2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(edit_info_locator))
        button_org2.click()

    def save_general_info(self):
        save_info_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[7]/button")
        button_org3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(save_info_locator))
        button_org3.click()

    #open qualifcations page/tab

    def click_qualification_button(self):
        button_qualification_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span")  # Initialise Locator
        button_qualification = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button_qualification_locator))
        button_qualification.click()

    def click_option_qualification(self):
        option_qualification_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]/a")  #
        button_qualification1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(option_qualification_locator))
        button_qualification1.click()


        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div.orangehrm-container > div > div.oxd-table-header > div > div:nth-child(2)")))
            assert True, "Open job page"
            print("qualification opened successfully")
        except TimeoutError:
            print("organization failed to open ")

    def qualification_add_button(self):
        qual_add_button_locator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button")  # I
        qual_add1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(qual_add_button_locator))
        qual_add1.click()

    def qualification_name(self,levelname):
        level_name_locator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-row > div > div:nth-child(2) > input")  # Initialise Locator
        level_name1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(level_name_locator))
        level_name1.send_keys(levelname)

    def qualification_save_button(self):
        qual_save_button_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")  # I
        qual_add2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(qual_save_button_locator))
        qual_add2.click()

    #open nationalities tab
    def click_open_nationalities(self):
        nationalities_locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a")
        national_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(nationalities_locator))
        national_btn.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div.orangehrm-header-container > h6")))
            assert True, "Open job page"
            print("nationalities opened successfully")
        except TimeoutError:
            print("organization failed to open ")

    #open corporate Branding
    def click_open_corporate_branding(self):
        corp_open_Locator = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a")
        corp_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(corp_open_Locator ))
        corp_btn.click()

#clicking the first clour(primary colour)
    def check_primary_color(self):
        corp_primary_Locator = (By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        corp_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(corp_primary_Locator))
        corp_btn1.click()

    def click_colour_present(self):
        clear_field_lacator = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div:nth-child(1) > div > div.orangehrm-color-input-wrapper > div > div.oxd-color-picker.--positon-left > input.oxd-color-picker-range")
        clear_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(clear_field_lacator))
        clear_btn1.click()

    def click_colour_present1(self):
        clear_field2_lacator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]")
        clear_away_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(clear_field2_lacator))
        clear_away_btn1.click()

   
#clicking the second colour
    def click_gradient_colour1(self):
        gradient_colour_lacator = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/div[2]/div/div")
        gradient_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(gradient_colour_lacator))
        gradient_btn1.click()

    def click_gradient_colour2(self):
        gradient_colour_lacator1 = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/div[2]/div/div[2]/input[1]")
        gradient_btn2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(gradient_colour_lacator1))
        gradient_btn2.click()

    def click_gradient_colour3(self):
        gradient_colour_lacator2 = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/div[2]/div/div[1]")
        gradient_btn3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(gradient_colour_lacator2))
        gradient_btn3.click()

    def publish_button(self):
        publish_button_locator = (By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > div > button.oxd-button.oxd-button--medium.oxd-button--secondary")  # I
        publish_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(publish_button_locator))
        publish_btn.click()

    #logout and log back in to verify that the colour has changed
    def profile_dropdown(self):
        dropdown_colour_lacator2 = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-userarea > ul > li > span")
        dropdown_btn5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(dropdown_colour_lacator2))
        dropdown_btn5.click()

    def profile_logout_option(self):
        logout_colour_lacator2 = (By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-userarea > ul > li > ul > li:nth-child(4) > a")
        logout_btn1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(logout_colour_lacator2))
        logout_btn1.click()


    def login_again_username(self,loginusername):
         login_username_locator = (By.NAME, "username")
         Login_username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login_username_locator))
         Login_username_input.send_keys(loginusername)

    def login_again_password(self,loginpassword):
         login_password_locator = (By.NAME, "password")
         Login_username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login_password_locator))
         Login_username_input.send_keys(loginpassword)

    def login_again(self):
         login_locator1 = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
         Login_input1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(login_locator1))
         Login_input1.click()

    def open_admin_again(self):
         admin_lacator2 = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
         admin_btn5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(admin_lacator2))
         admin_btn5.click()


    def click_corporate_branding_again(self):
         click_corp_again_lacator2 = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a")
         branding_btn5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable( click_corp_again_lacator2 ))
         branding_btn5.click()


    def Reset_to_default(self):
        reset_lacator2 = (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[1]")
        reset_btn5 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(reset_lacator2))
        reset_btn5.click()

    
