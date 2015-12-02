# herokuapp_conftest.py

# ==================
# REFERENCE/TEMPLATE
# ==================
# Contains lots of compelling boiler plate I can't take credit for.

# The purpose of this file is to configure our test environment.


import pytest
import time


# Modifies selenium to add a 5 second wait before failing out and 
# maximizes the browser.
@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(5)
    selenium.maximize_window()
    return selenium


# Work around for sensitive environments.  This saves us from flagging
# tests with @pytest.mark.nondestructive.
def pytest_addoption(parser):
    parser.addoption("--url", action = "store", help = "Target URL")


# Goes to the website specified (or a default website if nothing is
# specified).
@pytest.fixture
    def navigate_to_site(selenium, request, variables):
        target_URL = request.config.getoption("--url")
        if target_URL = None:
            target_URL = variables["default_url"]
        selenium.get(target_URL)