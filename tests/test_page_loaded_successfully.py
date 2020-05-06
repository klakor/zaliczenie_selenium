import sys, os
sys.path.append("..")
from base_test import BaseTest
from pages.login_page import LoginPage
from locators import LoginPageLocators
import unittest
import HtmlTestRunner

class LoginPageTest(BaseTest):
    """
    Testy strony startowej inpost.pl
    """
    def test_page_loaded_successfully(self):
        """Test prawidłowego załadowania się strony"""

        assert "Paczkomaty.pl" in self.driver.title

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
