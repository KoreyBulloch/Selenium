# test_herokuapp_login.py

# Performs a login at https://the-internet.herokuapp.com/login


import pytest
import time


# Verify that login is successful with correct credentials.
def test_login_success(selenium, variables):
    # Click on "Form Authentication"
    selenium.find_element_by_xpath(variables["form_auth_link"]).click()
    # Select Username field and enter correct username.
    selenium.find_element_by_xpath(variables["username_field"]).send_keys(variables["username_text"])
    # Select Password field and enter correct password.
    selenium.find_element_by_xpath(variables["password_field"]).send_keys(variables["password_text"])
    # Click on the Login button
    selenium.find_element_by_xpath(variables["login_button"]).click()
    # Verify that login was successful by checking page text for
    # "Welcome to the Secure Area. When you are done click logout below."
    assert selenium.find_element_by_xpath(variables["login_success_element"]).\
    text == variables["login_success_text"]