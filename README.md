This repository contains tests of https://inpost.pl/ website.

Test cases are written using selenium and unnittest frameworks. 
Test data for registration and login pages are imported from dedicated *.csv files using ddt module.
Test reports are generated using HtmlTestRunner module and saved automatically in '/reports' folder.

Make sure that you have the chromedriver installed. If not, you can download it here:
https://chromedriver.chromium.org/downloads

All required dependencies are provided in test_requirements.txt file.
You can install them by running a single command:
$ make deps

A test_suite.py is provided in '/tests' folder. You can run it directly or use the command:
$ make test

So far, the following tests are available:
- verification if home, login and register pages loaded succesfully
- navigation between home, login and register pages
- registration - failed
- logging - failed
- logging - succeded
