from selenium import webdriver


driver = ''


class BrowserInitialization:

    @staticmethod
    def generateDriver(browser, url):
        global driver
        if browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'edge':
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver
