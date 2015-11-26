#! python3

# conftest.py
# Configure test file

# ==================
# REFERENCE/TEMPLATE
# ==================
# Contains lots of compelling boiler plate I can't take credit for.


import pytest
import time


# Modifies selenium a bit to add a 5 second wait before failing as page
# items will sometimes be shy at first, and increases window size.
@pytest.fixture
def selenium(selenium):
    # Wait 5 seconds before calling it bad, much like floor food. Gross.
    selenium.implicitly_wait(5)
    # Maximizes window size, if you're into that sort of thing.
    selenium.maximize_window()
    # Returns the modified selenium value.
    return selenium


# Adding option to "parser" because of sensitive environments in
# pytest-selenium, which flags test as destructive by default.  Since
# we are men and women of action, we're skipping the 
# @pytest.mark.nondestructive.  How exactly this does that remains to be
# properly explained, but I'm certain we'll regret this later.
# Revisit this soon.
def pytest_addoption(parser):
    parser.addoption("--url", action = "store", help = "target URL")


# Goes to the website specified (or a default website if nothing is
# specified).
@pytest.fixture(scope = "function", autouse = True)
def navigate_to_site(selenium, request, variables):
    # Set the target URL to whatever we put after --url.
    target_URL = request.config.getoption("--url")
    # If we didn't specify --url, use a default URL from variables.
    if target_URL == None:
        target_URL = variables["default_url"]
    # Go to the website.
    selenium.get(target_URL)


# Goes through the login process.
@pytest.fixture(scope = "function")
def login(selenium, request, variables):
    # Steps to login go here.
    # Example:
    # selenium.find_element_by_xpath(".//*[@id='loginDropdown']").click()
    # selenium.find_element_by_xpath(".//*[@id='login-email']").send_keys("extremecatenthusiast@cats.com")
    # selenium.find_element_by_xpath(".//*[@id='login-password']").send_keys("8livesLeft")
    # selenium.find_element_by_xpath(".//*[@id='login-submit']").click() 