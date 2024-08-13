import time
from _ast import And

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# import Features.Steps.Fwu_Login
from Elements import fwu_login_elements
from Inputs import fwu_login_inputs
from Elements import fwu_logout_elements
from Elements import fwu_userimport_elements
from Inputs import fwu_userimport_inputs
from generic_methods.reusable_methods import *
from generic_methods import reusable_methods
# from Features.Steps.Fwu_Login import login
import pandas as pd
from Fwu_Login import *

# Initialize MyWebDriver object
web_driver = MyWebDriver()

@given(u'logged in from admin user')
def login_user_import(context):
    login(context)

@when(u'file imported with user unique data')
def userimport(context):

    #open the menu on dashboard
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(1)

    #Navigate to Administration -> User management
    reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.admin_menu_open)
    reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.um_menu_open)
    time.sleep(8)
    capture_screenshot(context)
    #reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_user_search, fwu_usercreation_inputs.searchuser)

    #Click on Import button appearing at user grid
    reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.button_userimport)
    capture_screenshot(context)
    time.sleep(3)

    # select file
    reusable_methods.input_action_woclear_xpath(context.driver, fwu_userimport_elements.textbox_importfile, fwu_userimport_inputs.file_path)
    time.sleep(4)

    #Click on Import dialogue
    reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.button_import_dialogue)
    time.sleep(10)

@then(u'user created/imported successfully')
def import_result(context):
        # text_pop = reusable_methods.assertion_xpath(context.driver, fwu_userimport_elements.message_validation).text
        # if text_pop == fwu_userimport_inputs.after_successful_import_Italian or text_pop == fwu_userimport_inputs.after_successful_import_English:
        #     time.sleep(2)
        #     capture_screenshot(context)
        #     assert True
        #
        # else:
        #     assert False

        reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.Button_dialogue_ok)
        time.sleep(1)
        reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.Button_dialogue_cancel)
        time.sleep(2)
        reusable_methods.click_action_xpath(context.driver, fwu_userimport_elements.Button_updategrid)
        time.sleep(5)

        #sheet name of excel file
        sheet_name = 'Users Report'

        #column name of excel file
        column_name = 'UserName'

        data = reusable_methods.read_column_data(fwu_userimport_inputs.file_path, sheet_name, column_name)
        reusable_methods.input_action_xpath(context.driver, fwu_userimport_elements.textbox_user_search, data)
        time.sleep(2)

        #logout
        reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
        time.sleep(2)
        reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout)
        reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout_yes)


