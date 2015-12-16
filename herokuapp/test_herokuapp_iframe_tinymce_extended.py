# test_herokuapp_iframe_tinymce_extended.py

# More interactions with TinyMCE at https://the-internet.herokuapp.com/tinymce


import pytest
import time


# Date/Time for time stamp.  Prints in format: YY-MM-DD_HHMM_SS
time_hours = time.strftime("%H%M_%S")
time_date = time.strftime("%Y-%m-%d")
time_stamp = time_date + "_" + time_hours


# Verify typed text after selecting Bold from the menu and typing in bold.
def test_tinymce_menu_bold_text(selenium, variables, util):
    # This will be used as part of the name for all screenshots taken for
    # this test.
    test_name = "TinyMCE_menu_bold_text_"
    # Checks for a screenshots folder in the current directory, and creates one if it is not found.
    util.check_and_create_screenshot_folder()
    # Click on "WYSIWYG Editor".
    selenium.find_element_by_xpath(variables["wysiwyg_editor_url"]).click()
    # Switching focus:
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    # Clear existing text in the TinyMCE text field.
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).clear()
    # Switching focus:
    # Go back to the webpage/default content.
    selenium.switch_to.default_content()
    # Click the "Format" menu.
    selenium.find_element_by_xpath(variables["format_menu"]).click()
    # Click on "Bold" in the Format menu.
    # Note: TinyMCE is a complete pain.  Button IDs seem to be generated
    # on load, names have spaces, and all sorts of other headaches.  For
    # this we're using XPath and text contains, which could be refined
    # by further specifying the XPath.
    selenium.find_element_by_xpath("//*[contains(text(), 'Bold')]").click()
    # Switching focus:
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    # Select the TinyMCE text field and type "Bold text is bold."
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).send_keys("Bold text is bold.")
    # Save a screenshot with our custom file name and time_stamp in the current working directory.
    # This has been disabled as it clutters the test folder, but it remains a good example.
    # selenium.save_screenshot(test_name + time_stamp + ".png")
    # Save a screenshot with our custom file name and time_stamp in a specific folder.
    # For this, the folder is "screenshots" in the test directory.  This will fail if the folder
    # is not present (but it's fair to assume that it will be, so I'm not bothering with a check).
    selenium.get_screenshot_as_file(util.os_safe_screenshot_path() + test_name + time_stamp + ".png")
    # Verify that we wrote "Bold text is bold." in TinyMCE.
    assert "Bold text is bold." in selenium.find_element_by_xpath(variables["tinymce_text_field"]).text


def test_tinymce_responsive_resize(selenium, variables, util):
    # This will be used as part of the name for all screenshots taken for
    # this test.
    test_name = "TinyMCE_responsive_resize_"
    # Checks for a screenshots folder in the current directory, and creates one if it is not found.
    util.check_and_create_screenshot_folder()
    # Click on "WYSIWYG Editor".
    selenium.find_element_by_xpath(variables["wysiwyg_editor_url"]).click()
    # Maximize window size (we do this by default with config, but this is how you would do it otherwise).
    selenium.maximize_window()
    # Save a screenshot with our custom file name and time_stamp in the "screenshots" folder.
    selenium.get_screenshot_as_file(util.os_safe_screenshot_path() + test_name + time_stamp + "_maximized" + ".png")
    # Set window size to 960x450.
    selenium.set_window_size(960, 450)
    # Save a screenshot with our custom file name and time_stamp in the "screenshots" folder.
    selenium.get_screenshot_as_file(util.os_safe_screenshot_path() + test_name + time_stamp + "_960x450" + ".png")
    # assert selenium.support.expected_conditions.visibility_of(variables[""])


def test_tinymce_button_italic_text(selenium, variables, util):
    # This will be used as part of the name for all screenshots taken for
    # this test.
    test_name = "TinyMCE_button_italic_text_"
    # Checks for a screenshots folder in the current directory, and creates one if it is not found.
    util.check_and_create_screenshot_folder()
    # Click on "WYSIWYG Editor".
    selenium.find_element_by_xpath(variables["wysiwyg_editor_url"]).click()
    # Switching focus:
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    # Clear existing text in the TinyMCE text field.
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).clear()
    # Switching focus:
    # Go back to the webpage/default content.
    selenium.switch_to.default_content()
    # Click the Italic button.
    # Note: TinyMCE is a complete pain.  Button IDs seem to be generated
    # on load, names have spaces, and all sorts of other headaches.  Since we can't trust
    # the ID, we're using XPath and the absolute path from a known constant ID.
    # It looks something like this:
    # .//*[@class='example']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/button
    selenium.find_element_by_xpath(variables["italic_button"]).click()
    # Switching focus:
    # Select TinyMCE iframe.
    selenium.switch_to.frame(selenium.find_element_by_xpath(variables["tinymce_iframe"]))
    # Select the TinyMCE text field and type "Italic text is italic."
    selenium.find_element_by_xpath(variables["tinymce_text_field"]).send_keys("Italic text is italic.")
    # Save a screenshot with our custom file name and time_stamp in the "screenshots" folder.
    selenium.get_screenshot_as_file(util.os_safe_screenshot_path() + test_name + time_stamp + ".png")
    # Verify that we wrote "Italic text is italic." in TinyMCE.
    assert "Italic text is italic." in selenium.find_element_by_xpath(variables["tinymce_text_field"]).text