# test_herokuapp_iframe_tinymce.py

# Interacts with TinyMCE at https://the-internet.herokuapp.com/tinymce


import pytest
import time


# Verify that we can use TinyMCE to write out "I <3 iframes".
def test_iframe_tinymce(selenium, variables):
    # Click on "WYSIWYG Editor".
    selenium.find_element_by_xpath(variables["wysiwyg_editor_url"]).click()
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    #
    # The interwebs likes to select iframes as shown below.
    # It works, but you'd need a [0], [1], etc. for multiple iframes.
    # selenium.switch_to.frame(selenium.find_element_by_tag_name("iframe"))
    #
    # To get back to the webpage, use the following:
    # selinium.switch_to.default_content()
    #
    # Select the TinyMCE text field and clear existing text.
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).clear()
    # Select the TinyMCE text field and type "I <3 iframes".
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).send_keys(variables["i_heart_iframe_text"])
    # Verify that we wrote "I <3 iframes" in TinyMCE.
    assert variables["i_heart_iframe_text"] in selenium.find_element_by_xpath(variables["tinymce_text_field"]).text