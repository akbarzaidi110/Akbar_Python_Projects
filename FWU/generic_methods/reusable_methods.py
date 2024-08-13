import os
import random
import string
import time
import logging

import allure

import time
import json
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from generic_methods.webdriver import MyWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd

#Take screenshots
def capture_screenshot(context):
    # Capture screenshot and save it in the "screenshots" directory
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    random_3_digit_number = random.randint(100, 999)
    ran_num = str(random_3_digit_number)
    screenshot_name = "screenshot" + ran_num + ".png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    context.driver.save_screenshot(screenshot_path)

    # Attach the screenshot to the Allure report
    with allure.step('Attach Screenshot'):
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG, name=screenshot_name)

#For entering data in element by clearing already available data first using locator Xpath
def input_action_xpath(driver, element, input):
    driver.find_element('xpath', element).clear()
    driver.find_element('xpath', element).send_keys(input)

#For entering data in element without clearing already available data using locator Xpath
def input_action_woclear_xpath(driver, element, input):
    driver.find_element('xpath', element).send_keys(input)

#For entering data in element by clearing already available data first using locator id
def input_action_id(driver, element, input):
    driver.find_element('id', element).clear()
    driver.find_element('id', element).send_keys(input)

#For entering data in element by clearing already available data first using locator name
def input_action_name(driver, element, input):
    driver.find_element('name', element).clear()
    driver.find_element('name', element).send_keys(input)

#For clicking an element using locator xpath
def click_action_xpath(driver, element):
    driver.find_element('xpath', element).click()

#For clicking an element using locator id
def click_action_id(driver, element):
    driver.find_element('id', element).click()

#For clicking an element using locator name
def click_action_name(driver, element):
    driver.find_element('name', element).click()

#For entering URL on browser
def get_url(driver, input):
    driver.get(input)

#For Asserting element using locator xpath
def assertion_xpath(driver, element):
    try:
        web_element = driver.find_element('xpath', element)
        return web_element
    except Exception as e:
        print(f"Error finding element by xpath: {element}. Error: {e}")
        return None

#For generating random passwords, writing it on text file and reading it from that file
def generate_password(length=8):
    random_3_digit_number = random.randint(100, 999)
    ran_num = str(random_3_digit_number)
    password_gen = "XYZxyz@" + ran_num
    return password_gen


def write_password_to_file(filename, password):
    """Write a password to a file."""
    with open(filename, 'w') as f:
        f.write(password)


def read_password_from_file(filename):
    """Read a password from a file."""
    with open(filename, 'r') as f:
        return f.read()

#For reading the data from Excel file
def read_column_data(file_path, sheet_name, column_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=2)
    return df[column_name]

#Wait until element is present
def wait_for_element(driver, by_locator, timeout=25):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(by_locator))

#Wait until alert is present
def wait_for_alert(driver, timeout=15):
    try:
        alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
        print("Alert is present!")
        return alert

    except TimeoutException:
        print(f"Alert not found within {timeout} seconds.")
        return None
