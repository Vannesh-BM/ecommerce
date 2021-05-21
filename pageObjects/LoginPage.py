import time

from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.HomePage import HomePage
from utilities import ScreenShot, ExcelUtil, PropertyFile


class LoginPage(BasePage):
    user_name = (By.XPATH, "//input[@id='user-name']")
    pwd = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    error_msg = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]")
    filter = (By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[2]/div[2]/span[1]/select[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password):
        global row
        try:
            self.clearAndType(self.user_name, username)
            self.clearAndType(self.pwd, password)
            self.click(self.login_button)
            print('************************',self.driver.title)
            self.presenceOfElement(self.filter)
            # ExcelUtil.write_data(PropertyFile.getValues('excelFilePath'),
            #                      PropertyFile.getValues('logintd'), row, 6,
            #                      "successful")
            # ExcelUtil.write_data(PropertyFile.getValues('excelFilePath'),
            #                      PropertyFile.getValues('logintd'), row, 7,
            #                      'Pass')
            # row = row + 3
            ScreenShot.takeScreenshot(self.driver, 'successfully_logged_in')
            return HomePage(self.driver)
        except:
            value = self.getText(self.error_msg)
            print('%%%%%%%%%%%%%%%%%%%%%',self.driver.title)
            # ExcelUtil.write_data(PropertyFile.getValues('excelFilePath'),
            #                      PropertyFile.getValues('logintd'), row, 6,
            #                      "unsuccessful")
            # ExcelUtil.write_data(PropertyFile.getValues('excelFilePath'),
            #                      PropertyFile.getValues('logintd'), row, 7,
            #                      'Pass')
            # row = row + 3
            return None
