import time

from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By

from utilities import ScreenShot


class OrderProduct(BasePage):
    checkout_button = (By.XPATH, "//button[@id='checkout']")
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_button = (By.XPATH, "//input[@id='continue']")
    finish_button = (By.XPATH, "//button[@id='finish']")
    back_to_home_button = (By.XPATH, "//button[@id='back-to-products']")

    def __init__(self, driver):
        super().__init__(driver)

    def order_product(self,firstname,lastname,postalcode):
        self.click(self.checkout_button)
        self.clearAndType(self.first_name, firstname)
        self.clearAndType(self.last_name, lastname)
        self.clearAndType(self.postal_code, postalcode)
        self.click(self.continue_button)
        self.click(self.finish_button)
        time.sleep(3)
        ScreenShot.takeScreenshot(self.driver, 'product_ordered_successfully')
        self.click(self.back_to_home_button)

