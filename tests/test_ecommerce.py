import time

import pytest
from pageObjects.LoginPage import LoginPage
from testData.TestData import TestData
from utilities import ExcelUtil, PropertyFile, ScreenShot
from utilities.BaseClass import BaseClass


class TestEcommerce(BaseClass):

    @pytest.mark.order(1)
    def test_ecommerce(self, getData):
        try:
            driver = self.driver
            logger = self.getLogger()

            loginpage = LoginPage(driver)

            homepage = loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
            logger.info('Logged In Successfully')

            orderproduct=homepage.go_to_cart()
            orderproduct.order_product(getData['firstname'],getData['lastname'],getData['postalcode'])
            logger.info('Product ordered successfully')

            # status = False
            # for key in getData:
            #     if getData[key] is None:
            #         status = True
            # if status:
            #     time.sleep(1.5)
            #     ScreenShot.takeScreenshot(driver, 'Error Occurred')
            #     raise Exception
            TestData.write_valid_result()
            homepage.menu_bar()
            homepage.do_logout()
            logger.info('Logged Out Successfully')
        except:
            logger.info('Order failed')
            TestData.write_invalid_result()
            homepage.menu_bar()
            homepage.do_logout()
            logger.info('Logged Out Successfully')
            assert False

    @pytest.fixture(params=TestData.getCustomerInformationTestData())
    def getData(self, request):
        return request.param
