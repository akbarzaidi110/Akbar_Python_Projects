from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Elements import fwu_logout_elements
from generic_methods import reusable_methods
def menu_open(driver, hamburger_menu_open):
     reusable_methods.click_action_xpath(driver, fwu_logout_elements.hamburger_menu_open)
     #driver.find_element('xpath', fwu_logout_elements.hamburger_menu_open).click()

def logout(driver, button_logout):
     reusable_methods.click_action_xpath(driver, fwu_logout_elements.button_logout)
     #driver.find_element('xpath', fwu_logout_elements.button_logout).click()
def logout_yes(driver, button_logout_yes):
     reusable_methods.click_action_xpath(driver, fwu_logout_elements.button_logout_yes)
     #driver.find_element('xpath', fwu_logout_elements.button_logout_yes).click()








