from selenium.webdriver.common.by import By


class PlaceOrder:

    add_backpack_id = "add-to-cart-sauce-labs-backpack"
    add_tshirt_id = "add-to-cart-sauce-labs-bolt-t-shirt"
    go_to_kart_xpath = "//span[@class='shopping_cart_badge']"
    check_out_id = "checkout"
    user_first_name_id = "first-name"
    user_last_name_id = "last-name"
    user_code_id = "postal-code"
    button_continue_id = "continue"
    button_finish_id = "finish"


    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(By.ID, self.add_backpack_id).click()

    def add_tshirt(self):
        self.driver.find_element(By.ID, self.add_tshirt_id).click()

    def click_kart_link(self):
        self.driver.find_element(By.XPATH, self.go_to_kart_xpath).click()

    def check_out_button(self):
        self.driver.find_element(By.ID, self.check_out_id).click()

    def enter_firstName(self,firstname):
        self.driver.find_element(By.ID, self.user_first_name_id).send_keys(firstname)

    def enter_lastName(self, lastname):
        self.driver.find_element(By.ID, self.user_last_name_id).send_keys(lastname)

    def enter_postalcode(self,postalcode):
        self.driver.find_element(By.ID, self.user_code_id).send_keys(postalcode)

    def click_con_button(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()

    def click_finish(self):
        self.driver.find_element(By.ID, self.button_finish_id).click()