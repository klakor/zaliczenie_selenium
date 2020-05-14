
import unittest

import HtmlTestRunner

from tests.test_inpost_homepage import HomePageTest
from tests.test_inpost_logging import LoggingNegative, LoggingPositive, LoggingNavigationTest
from tests.test_inpost_quicksend import QuickSendNavigationTest, QuickSendNegative
from tests.test_inpost_registration import RegistrationNavigationTest, RegistrationTest


class TestSuite(unittest.TestSuite):
    """
    All inpost.pl tests
    """

    def suite(self):
        suite = unittest.TestSuite()
        # Class name('test name')
        suite.addTest(HomePageTest('test_home_page_loaded_successfully'))
        suite.addTest(RegistrationNavigationTest('test_navigate_to_register_page'))
        suite.addTest(RegistrationTest('test_registration_negative'))
        suite.addTest(LoggingNavigationTest('test_navigate_to_login_page'))
        suite.addTest(LoggingNegative('test_logging_negative'))
        suite.addTest(LoggingPositive('test_logging_positive'))
        suite.addTest(QuickSendNavigationTest('test_navigate_to_quicksend_page'))
        suite.addTest(QuickSendNegative('test_quicksend_negative'))

        return suite


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
