# test_herokuapp_key_presses.py

# Presses the "Shift" key at https://the-internet.herokuapp.com/key_presses


import pytest
import time
from selenium.webdriver.common.keys import Keys


# Verify that we successfully report that the "Shift" key was pressed.
def test_dropdown_option2(selenium, variables):
    # Click on "Key Presses".
    selenium.find_element_by_xpath(variables["key_presses_url"]).click()
    # Press the "Shift" key.
    selenium.send_keys(variables["key_press"])
    # Verify that we report "Shift" as being pressed.
    assert selenium.find_element_by_xpath(variables["key_result"]).\
    text == variables["key_text"]