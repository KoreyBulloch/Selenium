# test_herokuapp_iframe_tinymce_extended.py

# More interactions with TinyMCE at https://the-internet.herokuapp.com/tinymce


import pytest
import time


# Date/Time for time stamp.  Prints in format: YY-MM-DD_HHMM_SS
time_hours = time.strftime("%H%M_%S")
time_date = time.strftime("%Y-%m-%d")
time_stamp = time_date + "_" + time_hours


# Clear text, select Bold from the Format menu, type "Bold text is bold",
# take a screenshot and save it with a time stamp in the name, and verify
# that we write "Bold text is bold".
def test_tinymce_menu_bold_text(selenium, variables, util):
    # This will be used as part of the name for all screenshots taken.
    test_name = "TinyMCE_menu_bold_text_"
    # Click on "WYSIWYG Editor".
    selenium.find_element_by_xpath(variables["wysiwyg_editor_url"]).click()
    # Switching focus:
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    # Select the TinyMCE text field and clear existing text.
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).clear()
    # Switching focus:
    # Go back to the webpage/default content
    selenium.switch_to.default_content()
    # Select the "Format" menu and click on it.
    selenium.find_element_by_xpath(variables["format_menu"]).click()
    # Select "Bold" from the Format menu and click on it.
    # Note: TinyMCE is a complete pain.  Button IDs seem to be generated
    # on load, names have spaces, and all sorts of other headaches.  For
    # this we're using XPath and text contains, which could be refined
    # by further specifying the XPath.
    selenium.find_element_by_xpath("//*[contains(text(), 'Bold')]").click()
    # Switching focus:
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    # Select the TinyMCE text field and type "I <3 iframes".
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).send_keys("Bold text is bold")
    # Save a screenshot with our custom file name and time_stamp.
    selenium.save_screenshot(test_name + time_stamp + ".png")
    # Save a screenshot with our custom file name and time_stamp to a specific folder,
    # (screenshots in the test directory).  This is PC only for now.
    selenium.get_screenshot_as_file(util.os_safe_screenshot_path() + test_name + time_stamp + ".png")
    # Verify that we wrote "I <3 iframes" in TinyMCE.
    assert "Bold text is bold" in selenium.find_element_by_xpath(variables["tinymce_text_field"]).text
