# herokuapp_utilities.py


import pytest
import os


class Util():
    
    def __init__(self, selenium, variables, request):
        self.selenium  = selenium
        self.variables = variables
        self.request = request


    def os_safe_screenshot_path(self):
        return os.path.join(self.variables["screenshot_path"])


    def check_and_create_screenshot_folder(self):
        if os.path.exists("screenshot") != True:
            os.makedirs("screenshot")