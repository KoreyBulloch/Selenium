# test_herokuapp_multiple_windows.py

# Dealing with tests that involve multiple windows.


import pytest
import time


# Verify URL after switching to another window.
def test_tinymce_menu_bold_text(selenium, variables):
    # Click on "Multiple Windows".
    selenium.find_element_by_xpath(variables["multiple_windows_url"]).click()
    # Click on "Click Here".
    selenium.find_element_by_xpath(variables["multiple_windows_click_here"]).click()
    # Switching focus:
    # Switch to the second web page.
    selenium.switch_to_window(selenium.window_handles[1])
    # Verify we are on the second web page by checking the URL.
    assert selenium.current_url == variables["multiple_windows_new_url"]