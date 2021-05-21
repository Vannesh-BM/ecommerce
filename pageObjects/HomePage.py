import time

from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.OrderProduct import OrderProduct
from utilities import ScreenShot


class HomePage(BasePage):
    menu_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    reset_button = (By.XPATH, "//a[@id='reset_sidebar_link']")

    logout_button = (By.XPATH, "//a[@id='logout_sidebar_link']")
    all_items = (By.XPATH, "//a[@id='inventory_sidebar_link']")
    cross_button = (By.XPATH, "//button[@id='react-burger-cross-btn']")
    my_cart = (By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def menu_bar(self):
        self.click(self.menu_button)

    def reset_app_state(self):
        self.click(self.reset_button)

    def do_logout(self):
        self.click(self.logout_button)
        time.sleep(3)
        ScreenShot.takeScreenshot(self.driver, 'opened_sales_app')

    def click_cross_button(self):
        self.click(self.cross_button)

    def show_all_items(self):
        self.click(self.all_items)

    def go_to_cart(self):
        self.click(self.my_cart)
        # assert True == self.check_text_presence(self.HEADING, 'Sales')
        # ScreenShot.takeScreenshot(self.driver, 'opened_sales_app')
        return OrderProduct(self.driver)
