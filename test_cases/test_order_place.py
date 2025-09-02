import time

from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import LoginAdminPage
from selenium import webdriver

from base_pages.Place_Order import PlaceOrder
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogMaker

driver = webdriver.Chrome()


class Test02PlaceOrder:
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    firstname = ReadConfig.get_valid_firstname()
    lastname = ReadConfig.get_valid_lastname()
    postalcode = ReadConfig.get_postalcode()
    logger = LogMaker.log_gen()
    logger1 = LogMaker.log_gen1()

    def test_place_order(self, setup):
        self.logger.info("***************Valid admin loging*******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        self.driver.get(self.admin_page_url)
        self.admin_lp = LoginAdminPage(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        if actual_dashboard_text == "Products":
            self.logger.info("***************Admin login is successful*******************")
            self.driver.save_screenshot("./screenshots/valid_admin_login.png")
            assert True
        else:
            self.logger.info("***************Admin login is unsuccessful*******************")
            assert False

        self.place_order = PlaceOrder(self.driver)
        self.place_order.add_backpack()
        self.place_order.add_tshirt()
        self.place_order.click_kart_link()
        self.place_order.check_out_button()
        self.place_order.enter_firstName(self.firstname)
        self.place_order.enter_lastName(self.lastname)
        self.place_order.enter_postalcode(self.postalcode)
        self.place_order.click_con_button()
        self.place_order.click_finish()
        actual_order_message = self.driver.find_element(By.XPATH, "//div[@id='checkout_complete_container']/h2").text
        expected_message = "Thank you for your order!"
        if actual_order_message == expected_message:
            self.logger.info("************* Order Place successfully *****************")
            assert True
            self.driver.quit()
        else:
            self.logger.info("************* Order Not Place *****************")
            assert False
            self.driver.quit()
