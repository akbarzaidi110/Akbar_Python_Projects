import time
from _ast import And

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Elements import fwu_login_elements
from Inputs import fwu_login_inputs
from Inputs import fwu_usercreation_inputs
from Inputs import fwu_ChangePassword_inputs
from Elements import fwu_logout_elements
from Elements import fwu_usercreation_elements
from Elements import fwu_ChangePassword_elements
from generic_methods.reusable_methods import *
from generic_methods import reusable_methods
from selenium import webdriver
from selenium.webdriver.common.by import By
from generic_methods.reusable_methods import wait_for_element

# Initialize MyWebDriver object
web_driver = MyWebDriver()

@when(u'user logged in with valid credential')
def login(context):
    #Hit the URL
    reusable_methods.get_url(context.driver, fwu_login_inputs.Url)
    context.driver.implicitly_wait(15)

    #Maximize the window
    context.driver.maximize_window()

    #Click on cancel button at pop up for PWA
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_id)

    #wait for username field to appear
    wait_for_element(context.driver, ('name', fwu_login_elements.textbox_username_name))

    #Enter username and password to login
    reusable_methods.input_action_name(context.driver, fwu_login_elements.textbox_username_name, fwu_login_inputs.username)
    reusable_methods.input_action_id(context.driver, fwu_login_elements.textbox_password_id, fwu_login_inputs.password)
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_login_id)

    alert = wait_for_alert(context.driver)  # Call the function to wait for alert
    if alert:
        alert.dismiss()  # Example action: dismiss the alert

    else:
        print("No alert to handle.")

    #time.sleep(4)
    #context.driver.switch_to.alert.dismiss()

    # wait for cancel button on welcome banner
    wait_for_element(context.driver, ('id', fwu_login_elements.button_cancel_message))
    #time.sleep(11)


    #Click on cancel button at welcome banner
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_message)
    capture_screenshot(context)
    time.sleep(2)

@then(u'user should be logged out successfully')
def logout(context):

    #open menu
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)

    time.sleep(1)
    #wait for logout menu
    wait_for_element(context.driver, ('xpath', fwu_logout_elements.button_logout))

    #logout application
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout)
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout_yes)

@when(u'user tries to login with invalid credential')
def login_failure(context):
    # Hit the URL
    reusable_methods.get_url(context.driver, fwu_login_inputs.Url)
    time.sleep(6)

    # Maximize the window
    context.driver.maximize_window()

    #Click on cancel button at pop up for PWA
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_id)

    # wait for username field to appear
    wait_for_element(context.driver, ('name', fwu_login_elements.textbox_username_name))

    # Enter incorrect username and password to login
    reusable_methods.input_action_name(context.driver, fwu_login_elements.textbox_username_name, fwu_login_inputs.username)
    reusable_methods.input_action_id(context.driver,fwu_login_elements.textbox_password_id,  fwu_login_inputs.invalidpassword)
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_login_id)

    wait_for_element(context.driver, ('xpath', fwu_login_elements.text_popupafterinvalidlogin_xpath))

@then(u'user should not be logged in')
def login_failure_result(context):
    text_pop = reusable_methods.assertion_xpath(context.driver, fwu_login_elements.text_popupafterinvalidlogin_xpath).text
    if text_pop == fwu_login_inputs.afterlogin_startup_text_italian or text_pop == fwu_login_inputs.afterlogin_startup_text_English:
        time.sleep(2)
        capture_screenshot(context)
        assert True

    else:
        assert False