from test_inpost_homepage import HomePageTest
from test_inpost_registration import RegistrationTest, NavigationTest
from test_inpost_logging import LoggingNegative, LoggingPositive, NavigationTest
from test_inpost_quicksend import NavigationTest, QuickSendNegative
import HtmlTestRunner

import unittest


class TestSuite(unittest.TestSuite):
    """
    All inpost.pl tests
    """

    def suite(self):
        suite = unittest.TestSuite()
        # Class name('test name')
        suite.addTest(HomePageTest('test_home_page_loaded_successfully'))
        suite.addTest(NavigationTest('test_navigate_to_register_page'))
        suite.addTest(RegistrationTest('test_registration_negative'))
        suite.addTest(NavigationTest('test_navigate_to_login_page'))
        suite.addTest(LoggingNegative('test_logging_negative'))
        suite.addTest(LoggingPositive('test_logging_positive'))
        suite.addTest(NavigationTest('test_navigate_to_quicksend_page'))
        suite.addTest(QuickSendNegative('test_quicksend_negative'))

        return suite


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
