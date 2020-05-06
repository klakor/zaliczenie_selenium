from test_page_loaded_successfully import LoginPageTest
from test_inpost_registration import RegistrationTest
from test_inpost_logging import LoggingTest

import unittest

class TestSuite(unittest.TestSuite):
    """
    Wszystkie testy strony Rejestracja
    """
    def suite():
        suite = unittest.TestSuite()
        # Nazwa klasy("nazwa testu")
        suite.addTest(LoginPageTest('test_page_loaded_successfully'))
        suite.addTest(RegistrationTest('test_registration'))
        suite.addTest(LoggingTest('test_logging_positive'))

        return suite

if __name__ == "__main__":
  unittest.main()
