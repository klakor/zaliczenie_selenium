from test_page_loaded_successfully import LoginPageTest, HomePageTest
from test_inpost_navigation import NavigationTest
from test_inpost_registration import RegistrationTest
from test_inpost_logging import LoggingNegative, LoggingPositive
import HtmlTestRunner

import unittest

class TestSuite(unittest.TestSuite):
    """
    Wszystkie testy strony Rejestracja
    """
    def suite():
        suite = unittest.TestSuite()
        # Nazwa klasy("nazwa testu")
        suite.addTest(HomePageTest('test_home_page_loaded_successfully'))
        suite.addTest(LoginPageTest('test_login_page_loaded_succesfully'))
        suite.addTest(NavigationTest('test_navigate_to_login_page'))
        suite.addTest(NavigationTest('test_navigate_to_register_page'))
        suite.addTest(LoggingNegative('test_logging_negative'))
        suite.addTest(LoggingPositive('test_logging_positive'))
        suite.addTest(RegistrationTest('test_registration'))
        suite.addTest(LoggingTest('test_logging_positive'))

        return suite

if __name__ == "__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
