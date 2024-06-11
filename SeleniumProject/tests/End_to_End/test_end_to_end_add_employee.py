import time
import pytest
from SeleniumProject.src.pages.PIMPage import PIMPage
from SeleniumProject.src.pages.Adminpage import Adminpage
from SeleniumProject.src.pages.MyInfoPage import MyInfoPage
from SeleniumProject.src.pages.DashboardPage import DashboardPage
from SeleniumProject.src.pages.Buzzpage import Buzzpage
from SeleniumProject.src.pages.Loginpage import Loginpage
import os

@pytest.mark.usefixtures('init_driver')
class TestEndToEndAddEmployee:

    @pytest.mark.suite1(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        pytest_html = item.config.pluginmanager.getplugin("html")
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, "extra", [])
        if report.when == "call":
            # always add url to report
            xfail = hasattr(report, "wasxfail")
            # check if test failed
            if (report.skipped and xfail) or (report.failed and not xfail):
                is_frontend_test = True if 'init_driver' in item.fixturenames else False
                if is_frontend_test:
                    results_dir = os.environ.get("RESULTS_DIR")
                    if not results_dir:
                        raise Exception("Environment variable 'RESULTS_DIR' must be set.")

                    screen_shot_path = os.path.join(results_dir, item.name + '.png')
                    driver_fixture = item.funcargs['request']
                    driver_fixture.cls.driver.save_screenshot(screen_shot_path)
                    # only add additional html on failure
                    # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
                    extra.append(pytest_html.extras.image(screen_shot_path))

            report.extra = extra

    @pytest.mark.suite1
    def test_invalid_login_details(self):
        Loginpage.go_to_page(self)
        time.sleep(3)
        Loginpage.input_login_username(self, "yvfufctf")
        time.sleep(2)
        Loginpage.input_login_password(self, "admin1234")
        time.sleep(2)
        Loginpage.click_login_button(self)
        time.sleep(5)
        Loginpage.verify_invalid_user(self)
        time.sleep(2)

    @pytest.mark.suite1
    def test_login_existing_user(self):

        Loginpage.input_login_username(self, "Admin")
        time.sleep(2)
        Loginpage.input_login_password(self, "admin123")
        time.sleep(2)
        Loginpage.click_login_button(self)
        time.sleep(3)
        Loginpage.verify_successful_login(self)
        time.sleep(2)

    #PIM page
    @pytest.mark.suite1
    def test_end_to_end_add_employee(self):

        PIMPage.click_pim_button(self)
        time.sleep(3)
        PIMPage.click_add_employee_button(self)
        time.sleep(3)
        PIMPage.employee_first_name(self,"Test1")
        time.sleep(3)
        PIMPage.employee_last_name(self,"lastname")
        time.sleep(3)
        PIMPage.employee_id(self,"4")
        time.sleep(3)
        PIMPage.create_login_details_button(self)
        time.sleep(3)
        PIMPage.input_login_username(self,"Thobeka7312")
        time.sleep(3)
        PIMPage.input_login_password(self, "Employee123User")
        time.sleep(4)
        PIMPage.match_login_password(self,"Employee123User")
        time.sleep(3)
        PIMPage.save_add_employee_button(self)
        time.sleep(5)


    #def test_cancel_adding_employee(self):
        # time.sleep(3)
        #PIMPage.click_add_employee_button(self)
        #time.sleep(3)
        #PIMPage.employee_first_name(self, "TestCancel")
        #time.sleep(3)
        #PIMPage.employee_last_name(self, "TestCancel")
        #time.sleep(3)
        #PIMPage.employee_id(self, "4")
        #.sleep(3)
        #PIMPage.cancel_employee(self)
        #time.sleep(4)

    @pytest.mark.suite1
    def test_search_user(self):
        #PIMPage.click_pim_button(self)
        #time.sleep(3)
        PIMPage.click_employee_list_button(self)
        time.sleep(3)
        PIMPage.employee_Search_name(self,"Test1")
        time.sleep(5)
        PIMPage.click_search_button(self)
        time.sleep(6)
        PIMPage.click_on_edit_button(self)
        time.sleep(4)

#admin page
    @pytest.mark.suite1
    def test_open_admin_page(self):

        Adminpage.click_admin_button(self)
        time.sleep(4)


    @pytest.mark.suite1
    def test_open_Job_page(self):

        Adminpage.click_job_button(self)
        time.sleep(5)
        Adminpage.click_option(self)
        time.sleep(5)

    @pytest.mark.suite1
    def test_add_employment_status_and_delete(self):

        Adminpage.click_add_button(self) #erroe
        time.sleep(5)
        Adminpage.employment_status_name(self,"Seasonal-worker")
        time.sleep(5)
        Adminpage.emp_save_button(self)
        time.sleep(5)
        Adminpage.delete_checkbox(self)
        time.sleep(5)
        Adminpage.delete_selected_message(self)
        time.sleep(4)
        Adminpage.delete_button_popup(self)
        time.sleep(4)

    #Organization page/tab
    @pytest.mark.suite1
    def test_open_organization_page(self):

         Adminpage.click_organization_checkbox(self)
         time.sleep(4)
         Adminpage.click_option_org(self)
         time.sleep(5)
         Adminpage.edit_general_info(self)
         time.sleep(5)
         Adminpage.save_general_info(self)
         time.sleep(5)

    #open qualifications page/tab
    @pytest.mark.suite1
    def test_open_and_add_qualification_page(self):

         Adminpage.click_qualification_button(self)
         time.sleep(4)
         Adminpage.click_option_qualification(self)
         time.sleep(5)
         Adminpage.qualification_add_button(self)
         time.sleep(5)
         Adminpage.qualification_name(self,"Higher Certificate")
         time.sleep(5)
         Adminpage.qualification_save_button(self)
         time.sleep(5)

    @pytest.mark.suite1
    def test_open_nationalities(self):
         Adminpage.click_open_nationalities(self)
         time.sleep(7)


    @pytest.mark.suite1
    #open nationalities
    def test_open_corporate_branding(self):
        Adminpage.click_open_corporate_branding(self)
        time.sleep(4)
        Adminpage.check_primary_color(self)
        time.sleep(5)
        Adminpage.click_colour_present(self)
        time.sleep(15)
        Adminpage.click_colour_present1(self)
        time.sleep(5)
        Adminpage.click_gradient_colour1(self)
        time.sleep(5)
        Adminpage.click_gradient_colour2(self)
        time.sleep(4)
        Adminpage.click_gradient_colour3(self)
        time.sleep(4)
        Adminpage.publish_button(self)
        time.sleep(4)
        Adminpage.profile_dropdown(self)
        time.sleep(6)
        Adminpage.profile_logout_option(self)
        time.sleep(4)
        Adminpage.login_again_username(self,"Admin")
        time.sleep(4)
        Adminpage.login_again_password(self,"admin123")
        time.sleep(4)
        Adminpage.login_again(self)
        time.sleep(4)
        Adminpage.open_admin_again(self)
        time.sleep(4)
        Adminpage.click_corporate_branding_again(self)
        time.sleep(4)
        Adminpage.Reset_to_default(self)
        time.sleep(6)



    #My Info Page
    @pytest.mark.suite3
    def test_my_info_page(self):
        #MyInfoPage.go_to_my_info_page(self)
        #time.sleep(4)
        #MyInfoPage.info_login_username(self,"Admin") #error
        #time.sleep(4)
        #MyInfoPage.info_login_password(self,"admin123")
        #time.sleep(4)
        #MyInfoPage.info_login_button(self)
        #time.sleep(4)
        MyInfoPage.info_button(self)
        time.sleep(3)
        MyInfoPage.contact_details(self)
        time.sleep(3)
        MyInfoPage.street_input(self,"354 Kent Avenu")
        time.sleep(3)
        MyInfoPage.city_input(self, "New York")
        time.sleep(3)
        MyInfoPage.state_input(self, "USA")
        time.sleep(3)
        MyInfoPage.zip_input(self,"8376")
        time.sleep(3)
        MyInfoPage.mobile_input(self,"083-8750-0943")
        time.sleep(3)
        MyInfoPage.save_contact_details(self)
        time.sleep(3)


    @pytest.mark.suite3
    def test_dashboard_page(self):

        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.click_time_at_work(self)
        time.sleep(4)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.quick_launch1(self)
        time.sleep(3)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.quick_launch2(self)
        time.sleep(3)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.quick_launch3(self)
        time.sleep(3)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.quick_launch4(self)
        time.sleep(3)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.quick_launch5(self)
        time.sleep(3)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.quick_launch6(self)
        time.sleep(3)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.buzz_page(self)
        time.sleep(4)
        DashboardPage.click_dashboard(self)
        time.sleep(3)
        DashboardPage.pie_chart(self)
        time.sleep(3)


    @pytest.mark.suite3
    def test_buzz_page(self):

        Buzzpage.click_buzz_page(self)
        time.sleep(3)
        Buzzpage.insert_commment(self,"motivation quotes")
        time.sleep(3)
        Buzzpage.post_button(self)
        time.sleep(3)
        Buzzpage.like_post(self)
        time.sleep(3)
        Buzzpage.share_post(self)
        time.sleep(3)
        Buzzpage.share_button(self)
        time.sleep(10)

















































        #Faith01











        #PIMPage.employee_Search_id(self,"")
        #time.sleep(3)












