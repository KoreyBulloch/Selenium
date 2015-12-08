# test_herokuapp_javascript_alerts.py

# Closes a JavaScript alert at https://the-internet.herokuapp.com/javascript_alerts


import pytest
import time


# Verify that we successfully accept the JavaScript alert.
def test_dropdown_option2(selenium, variables):
    # Click on "JavaScript Alerts".
    selenium.find_element_by_xpath(variables["javascript_alerts_url"]).click()
    # Click on "Click for JS Confirm".
    selenium.find_element_by_xpath(variables["click_for_js_confirm"]).click()
    # Switch to the alert and accept it.
    selenium.switch_to.alert.accept()
    # Confirm that we get the "You clicked: Ok" message.
    assert selenium.find_element_by_xpath(variables["click_result"]).\
    text == variables["click_result_confirm_text"]
