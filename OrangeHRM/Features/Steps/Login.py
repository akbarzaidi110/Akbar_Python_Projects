import time

import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Elements import login_elements, Admin_elements
from Generic_Methods.web_driver import desktopdriver

from Generic_Methods import web_driver
from Inputs import login_inputs


@when(u'a user provides valid login credential')
def login(context):
    context.driver = desktopdriver(context)
    #Hit the URL on browser
    web_driver.open_url_web(context.driver, 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #Maximize the window
    web_driver.maximize_window_web(context.driver)

    #Wait
    web_driver.implicit_wait_web(context.driver, 10)
    time.sleep(5)

    #Enter Username and password
    web_driver.input_action_web(context.driver, login_elements.Username_textbox, login_inputs.username)
    web_driver.input_action_web(context.driver, login_elements.password_textbox, login_inputs.password)
    web_driver.click_action_web(context.driver, login_elements.submit_button)
    time.sleep(5)

@then(u'user should be able to login')
def success_login(context):
    textpop = web_driver.assertion_xpath(context.driver,login_elements.dashboard_header).text
    if textpop == login_inputs.loginverification_text:
        time.sleep(2)
        web_driver.capture_screenshot(context)
        assert True

    else:
        time.sleep(2)
        web_driver.capture_screenshot(context)
        assert False

    #Click on Admin menu
    web_driver.click_action_web(context.driver, Admin_elements.Admin_menu)
    time.sleep(2)
