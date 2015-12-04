# test_herokuapp_dropdown.py

# Clicks on option 2 at https://the-internet.herokuapp.com/dropdown


import pytest
import time


# Verify that we successfully select option 2 from the dropdown.
def test_dropdown_option2(selenium, variables):
    # Click on "Form Authentication"
    selenium.find_element_by_xpath(variables["dropdown_url"]).click()
    # Unfortunately the dropdown on this page does nothing.  Sleeps are
    # added so the dropdown selection can be observed.
    time.sleep(1)
    # Select option 2 on the dropdown and click
    selenium.find_element_by_xpath(variables["dropdown_option2"]).click()
    # Wait added so a user can observe the process. 
    time.sleep(2)


    # The key here is the selection:
    # //select[@id='dropdown']/option[@value='2']