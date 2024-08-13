from selenium import webdriver
from Elements import fwu_login_elements
from Inputs import fwu_login_inputs
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from generic_methods import reusable_methods



def get_url(driver, Url):
     driver.get(fwu_login_inputs.Url)

def cancel_popup(driver, button_cancel_id):
     reusable_methods.click_action_id(driver, fwu_login_elements.button_cancel_id)
     #driver.find_element('id', fwu_login_elements.button_cancel_id).click()

def enter_username(driver, textbox_username_name ,input ):
     reusable_methods.input_action_name(driver, fwu_login_elements.textbox_username_name, fwu_login_inputs.username)
     #driver.find_element('name', fwu_login_elements.textbox_username_name).send_keys(fwu_login_inputs.username)

def enter_password(driver, textbox_password_id,input):
     reusable_methods.input_action_id(driver, fwu_login_elements.textbox_password_id, fwu_login_inputs.password)
     #driver.find_element('id', fwu_login_elements.textbox_password_id).send_keys(fwu_login_inputs.password)

def enter_incorrect_password(driver, textbox_password_id, input):
     reusable_methods.input_action_id(driver, fwu_login_elements.textbox_password_id, fwu_login_inputs.invalidpassword)
     #driver.find_element('id', fwu_login_elements.textbox_password_id).send_keys(fwu_login_inputs.invalidpassword)

def login_button_click(driver, button_login_id):
     reusable_methods.click_action_id(driver, fwu_login_elements.button_login_id)
     #driver.find_element('id', fwu_login_elements.button_login_id).click()

def cancel_message(driver, button_cancel_message):
     reusable_methods.click_action_id(driver, fwu_login_elements.button_cancel_message)
     #driver.find_element('id', fwu_login_elements.button_cancel_message).click()







