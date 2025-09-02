## Any pytest file should start with test_ or end with _test
## pytest method names should start with test
## Any code should be wrapped in method only
## In pytest every method treated as a testcase
## Method name should have sense
## -k stands for method names execution, -s logs in output, -v stands for more info like metadata

import time

from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import LoginAdminPage
from selenium import webdriver

from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker


driver = webdriver.Chrome()

class Test01AdminLogin:

    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_username()
    password =ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    logger = LogMaker.log_gen()
    logger1 = LogMaker.log_gen1()


    def test_title_verification(self, setup):
        self.logger.info("****************Test_01_Admin_Login********************")
        self.logger1.warning("**check for the warning**")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        expected_name = "Swag Labs"
        actual_title = self.driver.title
        if actual_title == expected_name:
            self.logger.info("***************Title verification is successful*******************")
            self.driver.save_screenshot("./screenshots/page_title.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("***************Title verification is unsuccessful*******************")
            self.driver.close()
            assert False


    def test_valid_admin_login(self, setup):
        self.logger.info("*************** Verify Valid admin loging*******************")
        self.driver = setup
        self.driver.implicitly_wait(4)
        self.driver.get(self.admin_page_url)
        self.admin_lp = LoginAdminPage(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH,"//span[@class='title']").text
        if actual_dashboard_text == "Products":
            self.logger.info("***************Admin login is successful*******************")
            self.driver.save_screenshot("./screenshots/valid_admin_login.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("***************Admin login is unsuccessful*******************")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self, setup):
        self.logger.info("***************InValid admin loging*******************")
        self.driver = setup
        self.driver.implicitly_wait(4)
        self.driver.get(self.admin_page_url)
        self.admin_lp = LoginAdminPage(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']/h3").text
        if actual_dashboard_text == "Epic sadface: Username and password do not match any user in this service":
            self.driver.save_screenshot("./screenshots/invalid_admin_login.png")
            self.logger.info("***************Invalid login is successful*******************")
            assert True
            self.driver.close()
        else:
            self.logger.info("***************Invalid login is unsuccessful*******************")
            self.driver.close()
            assert False
        self.driver.quit()
