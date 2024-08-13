import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Elements import fwu_usercreation_elements
from Inputs import fwu_usercreation_inputs
from generic_methods import reusable_methods

def menu_admin(driver, admin_menu_open):
     reusable_methods.click_action_xpath(driver, fwu_usercreation_elements.admin_menu_open)
def menu_um(driver, um_menu_open):
     reusable_methods.click_action_xpath(driver, fwu_usercreation_elements.um_menu_open)

# def user_search(driver, textbox_user_search):
#      reusable_methods.click_action_xpath(driver, fwu_usercreation_elements.textbox_user_search)

def enter_user_search(driver, textbox_user_search, input):
     time.sleep(2)
     reusable_methods.input_action_xpath(driver, fwu_usercreation_elements.textbox_user_search,fwu_usercreation_inputs.searchuser)








