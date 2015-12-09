# test_herokuapp_iframe_tinymce_extended.py

# More interactions with TinyMCE at https://the-internet.herokuapp.com/tinymce


import pytest
import time


# Date/Time for time stamp
time_hours = time.strftime("%H_%M_%S")
time_date = time.strftime("%Y-%m-%d")
time_stamp = time_date + "_" + time_hours


# Verify that we can use TinyMCE to write out "I <3 iframes".
def test_iframe_tinymce(selenium, variables):
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
    # Save a screenshot with our time_stamp custom file name.
    selenium.save_screenshot("TinyMCE_bold_text_" + time_stamp + ".png")
    # Verify that we wrote "I <3 iframes" in TinyMCE.
    assert "Bold text is bold" in selenium.find_element_by_xpath(variables["tinymce_text_field"]).text



    # Click on italic
    # selenium.find_element_by_xpath(".//*[@id='mceu_4']/button").click()