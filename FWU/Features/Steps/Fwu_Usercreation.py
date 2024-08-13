import time
from _ast import And

from behave import *
from selenium import webdriver
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

# Initialize MyWebDriver object
web_driver = MyWebDriver()

@given(u'NIMDA user logged in with valid credential')
def login(context):
    reusable_methods.get_url(context.driver, fwu_login_inputs.Url)
    context.driver.implicitly_wait(15)

    context.driver.maximize_window()

    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_id)
    time.sleep(8)
    reusable_methods.input_action_name(context.driver, fwu_login_elements.textbox_username_name, fwu_login_inputs.username)
    reusable_methods.input_action_id(context.driver, fwu_login_elements.textbox_password_id, fwu_login_inputs.password)
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_login_id)
    time.sleep(9)
    #context.driver.switch_to.alert.dismiss()
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_message)
    capture_screenshot(context)
    time.sleep(2)

@when(u'created a Market Admin user')
def usercreation(context):
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(1)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.admin_menu_open)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.um_menu_open)
    time.sleep(8)
    capture_screenshot(context)
    #reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_user_search, fwu_usercreation_inputs.searchuser)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.button_Add)
    time.sleep(1)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.button_cancel_user)
    time.sleep(1)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.button_Add)
    time.sleep(8)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.radiobutton_enabled)
    reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_username, fwu_usercreation_inputs.username)
    reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_password, fwu_usercreation_inputs.password)
    reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_confirmpassword, fwu_usercreation_inputs.confirmpassword)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.dropdown_salutation)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.dropdown_Mr_salutation)

@then(u'User created successfully')
def step_impl(context):
    pass



