import sys
sys.path.append("..")
from base_test import BaseTestHome, BaseTestLogin
from pages.home_page import HomePage
from pages.login_page import LoginPage
import unittest
import HtmlTestRunner

class HomePageTest(BaseTestHome):
    """
    Testy strony startowej inpost.pl
    """
    def test_home_page_loaded_successfully(self):
        """Test prawidłowego załadowania się strony domowej inpost.pl"""

        assert "InPost dla Ciebie" in self.driver.title


class LoginPageTest(BaseTestLogin):
    def test_login_page_loaded_succesfully(self):
        """Test przechodzenia na stronę manager paczek"""
        header_text = ("Zaloguj się do swojego konta")

        lp = LoginPage(self.driver)
        lp.verify_login_page_loaded_successfully(header_text)

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
