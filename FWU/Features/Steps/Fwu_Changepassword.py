import time
from _ast import And

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Elements import fwu_login_elements
from Functions.fwu_logout_functions import logout
from Inputs import fwu_login_inputs
from Inputs import fwu_usercreation_inputs
from Inputs import fwu_ChangePassword_inputs
from Elements import fwu_logout_elements
from Elements import fwu_usercreation_elements
from Elements import fwu_ChangePassword_elements
from generic_methods.reusable_methods import *
from generic_methods.webdriver import *
from generic_methods import reusable_methods
from generic_methods.reusable_methods import MyWebDriver
from generic_methods.reusable_methods import generate_password
from Fwu_Login import *

# Initialize MyWebDriver object
web_driver = MyWebDriver()

@given(u'logged in with nimda user')
def login_CP(context):
    login(context)

@when(u'changing the password of market admin user')
def changepassword(context):

    # Open menu
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(1)

    # Open User management page
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.admin_menu_open)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.um_menu_open)
    time.sleep(8)

    # Search and select a market admin user
    reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_user_search, fwu_usercreation_inputs.searchuser)
    time.sleep(2)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.radiobutton_uselection)
    time.sleep(1)
    # Click on change password button
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepwd)

    password = generate_password()
    print("Generated Password:", password)

    # Specify the file path
    filename = 'master_password.txt'

    write_password_to_file(filename, password)
    print("Password written to file.")

    # Read the password from the file
    read_password = read_password_from_file(filename)
    print("Read Password:", read_password)

    # Enter New password and confirm password & click on change password button
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_newpwd, read_password)
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_cnfmpwd, read_password)
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepassword)
    time.sleep(1)
    capture_screenshot(context)

    # Click on change password success message
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_chngpwdconfrm)
    time.sleep(8)

    # Logout the user
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(2)
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout)
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout_yes)
    time.sleep(6)

@then(u'market admin user logged in successfully')
def step_impl(context):

    # Specify the file path
    filename = 'master_password.txt'

    # Read the password from the file
    read_password = read_password_from_file(filename)
    print("Read Password:", read_password)

    # Enter the market admin credential and login to verify new password
    reusable_methods.input_action_name(context.driver, fwu_login_elements.textbox_username_name, fwu_ChangePassword_inputs.marketadminuser)
    reusable_methods.input_action_id(context.driver, fwu_login_elements.textbox_password_id, read_password)
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_login_id)
    time.sleep(9)
    capture_screenshot(context)
    # context.driver.switch_to.alert.dismiss()

    # Cancel the welcome message
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_message)
    capture_screenshot(context)
    time.sleep(2)

    # Logout the user
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(2)
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout)
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.button_logout_yes)

@given(u'user logged in successfully')
def login_CP2(context):

    #Hit the Application URl
    reusable_methods.get_url(context.driver, fwu_login_inputs.Url)

    context.driver.implicitly_wait(15)

    context.driver.maximize_window()

    #Cancel the pwa popup
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_id)
    time.sleep(8)

    # Enter User name and Password
    reusable_methods.input_action_name(context.driver, fwu_login_elements.textbox_username_name, fwu_login_inputs.username)
    reusable_methods.input_action_id(context.driver, fwu_login_elements.textbox_password_id, fwu_login_inputs.password)

    # Click on Login Button
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_login_id)
    time.sleep(9)

    # Dismiss the alert
    #context.driver.switch_to.alert.dismiss()

    #Cancel the welcome message
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_message)
    capture_screenshot(context)
    time.sleep(2)

@when(u'changing the password by entering less than 8 characters')
def changepwd(context):
     # Open menu
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(1)

    # Open User management page
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.admin_menu_open)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.um_menu_open)
    time.sleep(8)

    # Search and select a market admin user
    reusable_methods.input_action_xpath(context.driver, fwu_usercreation_elements.textbox_user_search, fwu_usercreation_inputs.searchuser)
    time.sleep(2)
    reusable_methods.click_action_xpath(context.driver, fwu_usercreation_elements.radiobutton_uselection)
    time.sleep(1)
    # Click on change password button
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepwd)

    # Enter New password and confirm password & click on change password button
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_newpwd, fwu_ChangePassword_inputs.password8)
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_cnfmpwd, fwu_ChangePassword_inputs.password8)
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepassword)
    time.sleep(2)

    text_popup = reusable_methods.assertion_xpath(context.driver, fwu_ChangePassword_elements.text_popupaftercharvalidation).text
    if text_popup == fwu_ChangePassword_inputs.eightcharvalidation_English or text_popup == fwu_ChangePassword_inputs.eightcharvalidation_Italian:
        time.sleep(2)
        capture_screenshot(context)
        assert True

    else:
        assert False

    # Click on change password failure message
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_chngpwdconfrm)
    time.sleep(2)

@when(u'when changing the password by entering incorrect combination')
def changepwd1(context):
    #Click to cancel change password dialogue
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_cancel)

    time.sleep(1)
    # Click on change password button
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepwd)

    # Enter New password and confirm password & click on change password button
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_newpwd, fwu_ChangePassword_inputs.passwordcomb)
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_cnfmpwd, fwu_ChangePassword_inputs.passwordcomb)
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepassword)
    time.sleep(2)

    text_popup = reusable_methods.assertion_xpath(context.driver, fwu_ChangePassword_elements.text_popupaftercharvalidation).text
    if text_popup == fwu_ChangePassword_inputs.combvalidation_Italian or text_popup == fwu_ChangePassword_inputs.combvalidation_English:
        time.sleep(2)
        capture_screenshot(context)
        assert True

    else:
        assert False

    # Click on change password failure message
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_chngpwdconfrm)

@when(u'when changing the password by entering from previously entered 24 passwords')
def changepwd2(context):

    #Click to cancel change password dialogue
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_cancel)

    time.sleep(1)
    # Click on change password button
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepwd)

    # Enter New password and confirm password & click on change password button
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_newpwd, fwu_ChangePassword_inputs.passwordlast)
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_cnfmpwd, fwu_ChangePassword_inputs.passwordlast)
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepassword)
    time.sleep(2)

    text_popup = reusable_methods.assertion_xpath(context.driver, fwu_ChangePassword_elements.text_popupaftercharvalidation).text
    if text_popup == fwu_ChangePassword_inputs.lasttfvalidation_Italian or text_popup == fwu_ChangePassword_inputs.lasttfvalidation_English:
        time.sleep(2)
        capture_screenshot(context)
        assert True

    else:
        assert False

    # Click on change password failure message
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_chngpwdconfrm)

@when(u'when changing the password by entering password which is obtain through personal information')
def changepwd3(context):

    #Click to cancel change password dialogue
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_cancel)

    time.sleep(1)
    # Click on change password button
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepwd)

    # Enter New password and confirm password & click on change password button
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_newpwd, fwu_ChangePassword_inputs.passwordknown)
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_cnfmpwd, fwu_ChangePassword_inputs.passwordknown)
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepassword)
    time.sleep(2)

    text_popup = reusable_methods.assertion_xpath(context.driver, fwu_ChangePassword_elements.text_popupaftercharvalidation).text
    if text_popup == fwu_ChangePassword_inputs.knownpassword_Italian or text_popup == fwu_ChangePassword_inputs.knownpassword_English:
        time.sleep(2)
        capture_screenshot(context)
        assert True

    else:
        assert False

    # Click on change password failure message
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_chngpwdconfrm)

@when(u'when changing the password by entering password which contains simple keyboard combinations')
def changepwd3(context):

     #Click to cancel change password dialogue
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_cancel)

    time.sleep(1)
    # Click on change password button
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepwd)

    # Enter New password and confirm password & click on change password button
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_newpwd, fwu_ChangePassword_inputs.passwordsimple)
    reusable_methods.input_action_xpath(context.driver, fwu_ChangePassword_elements.button_cnfmpwd, fwu_ChangePassword_inputs.passwordsimple)
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_changepassword)
    time.sleep(2)

@then(u'validation error appears')
def error(context):

    text_popup = reusable_methods.assertion_xpath(context.driver,
                                                  fwu_ChangePassword_elements.text_popupaftercharvalidation).text
    if text_popup == fwu_ChangePassword_inputs.simplepassword_Italian or text_popup == fwu_ChangePassword_inputs.simplepassword_English:
        time.sleep(2)
        capture_screenshot(context)
        assert True

    else:
        assert False

    # Click on change password failure message
    reusable_methods.click_action_xpath(context.driver, fwu_ChangePassword_elements.button_chngpwdconfrm)
    time.sleep(2)
    context.driver.quit()

@given(u'logged in with market admin user')
def login_CP3(context):

    # Hit the Application URl
    reusable_methods.get_url(context.driver, fwu_login_inputs.Url)

    # Cancel the pwa popup
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_id)
    time.sleep(8)

    # Specify the file path
    filename = 'master_password.txt'

    # Read the password from the file
    read_password = read_password_from_file(filename)
    print("Read Password:", read_password)

    # Enter User name and Password
    reusable_methods.input_action_name(context.driver, fwu_login_elements.textbox_username_name, fwu_login_inputs.marketadminuser)
    reusable_methods.input_action_id(context.driver, fwu_login_elements.textbox_password_id, read_password)

    # Click on Login Button
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_login_id)
    time.sleep(9)

    # Dismiss the alert
    # context.driver.switch_to.alert.dismiss()

    # Cancel the welcome message
    reusable_methods.click_action_id(context.driver, fwu_login_elements.button_cancel_message)
    capture_screenshot(context)
    time.sleep(2)


@when(u'changing the password of available market admin user')
def changepassword4(context):

    # Open menu
    reusable_methods.click_action_xpath(context.driver, fwu_logout_elements.hamburger_menu_open)
    time.sleep(1)

@then(u'market admin user logged in with changed password')
def login_CP4(context):
    pass