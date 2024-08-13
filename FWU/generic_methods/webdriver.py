from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class MyWebDriver:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        # self.driver.implicitly_wait(15)
        # self.driver.maximize_window()
        return self.driver
