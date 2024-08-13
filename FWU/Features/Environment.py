from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from generic_methods.reusable_methods import MyWebDriver

def before_all(context):
    pass
def after_all(context):
    pass

def before_scenario(context, scenario):
    context.web_driver = MyWebDriver()
    context.driver = context.web_driver.initialize_driver()
def after_scenario(context, scenario):
    # context.driver.quit()

    pass