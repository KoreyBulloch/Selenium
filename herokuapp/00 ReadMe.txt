Requirements:
=============

1) Python 3.x
2) py.test-selenium (includes selenium and py.test)



Setup:
======

An updated version of pytest_variables.py is required for this to run:

1) Copy pytest_variables.py in the installation folder.
2) Overwrite and paste pytest_variables.py in PythonInstallationFolder\Lib\site-packages\pytest_variables.py



Execution:
==========

In a command prompt, run the following:

py.test.exe --driver Firefox --variables .\herokuapp_variables.json



Driver options:
---------------
Chrome *
Firefox
IE *

BrowserStack
PhantomJS
Remote
SauceLabs
TestingBot


* Chrome and IE need drivers specified, IE needs to be configured:
$ py.test --driver Chrome --driver-path /path/to/chromedriver
> py.test --driver IE --driver-path \path\to\IEDriverServer.exe

http://pytest-selenium.readthedocs.org/en/latest/user_guide.html#chrome