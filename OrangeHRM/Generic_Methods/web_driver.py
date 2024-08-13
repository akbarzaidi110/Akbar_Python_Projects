import os
import random

import allure
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def desktopdriver(context):
    # Create a WebDriver instance
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option('detach', True)
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #context.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(10)
    return context.driver

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
#
# driver=None

def open_url_web(driver, url):
    driver.get(url)
def maximize_window_web(driver):
    driver.maximize_window()

def implicit_wait_web(driver, seconds):
    driver.implicitly_wait(seconds)

def input_action_web(driver, element, input):
    driver.find_element('xpath', element).clear()
    driver.find_element('xpath', element).send_keys(input)

def input_empty_web(driver, element, input):
    element_w = driver.find_element('xpath', element)
    element_w.send_keys(Keys.CONTROL + 'a')
    element_w.send_keys(Keys.BACKSPACE)
    element_w.send_keys(input)


#For entering data in element without clearing already available data using locator Xpath
def input_action_woclear_xpath(driver, element, input):
    driver.find_element('xpath', element).send_keys(input)


def click_action_web(driver, element):
    driver.find_element('xpath', element).click()

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


#For generating random username
def generate_uname(length=11):
    random_3_digit_number = random.randint(100, 999)
    ran_num = str(random_3_digit_number)
    uname_gen = "automate." + ran_num
    return uname_gen


#For generating random firstname and last name
# Function to generate unique names
first_names = [
    "Akbar", "Baqir", "safwan", "zeeshan", "farooq", "neel", "raheel", "faisal",
    "saleem", "abid", "murtaza", "rehan", "adnan", "hasan", "asad", "tahir",
    "bharat", "saquib", "aadil", "saad", "imran", "ghufran", "waqar", "ali",
    "ashraf", "faizan"
]

last_names = [
    "raza", "rizvi", "mouazzam", "khan", "Ali", "kamal", "Ahmed",
    "Mukhtar", "hussain", "ghulam", "hameed", "jaffery", "farooqui",
    "kumar", "sami", "khan", "ashfaque", "zaidi", "hashmi",
    "iqbal", "noorani", "ismail", "ameen", "Lee", "Walker", "Hall"
]

# Set to keep track of generated names
used_names = set()


def generate_unique_name():
    global name_first, name_last  # Access global variables inside the function
    while True:
        # Randomly select a first name and a last name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        # Combine the first name and last name
        full_name = f"{first_name} {last_name}"

        # Check if the generated name is unique
        if full_name not in used_names:
            used_names.add(full_name)
            name_first = first_name  # Assign to global variable
            name_last = last_name  # Assign to global variable
            return first_name, last_name


for _ in range(10):
    first_name, last_name = generate_unique_name()

#For generating random salesagentcode (Solyda)
def generate_sacode(length=8):
    random_3_digit_number = random.randint(100, 999)
    ran_sacode = str(random_3_digit_number)
    sacode_gen = "85024" + ran_sacode
    return sacode_gen
