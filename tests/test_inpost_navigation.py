from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage
import unittest
import HtmlTestRunner

from tests.base_test import BaseTestHome


class NavigationTest(BaseTestHome):
    def test_navigate_to_login_page(self):
        """Test przechodzenia na stronę manager paczek"""
        header_text = ("Zaloguj się do swojego konta")

        hp = HomePage(self.driver)
        # hp.close_covid_popup()
        hp.click_sign_in_btn()
        hp.click_manager_paczek_btn()
        hp.switch_driver_to_active_tab()

        lp = LoginPage(self.driver)
        # lp.refresh()
        lp.verify_login_page_loaded_successfully(header_text)

    def test_navigate_to_register_page(self):
        """Test przechodzenia na stronę rejestracji użytkownika"""
        header_text = ("Rejestracja")

        hp = HomePage(self.driver)
        # hp.close_covid_popup()
        hp.click_sign_in_btn()
        hp.click_manager_paczek_btn()
        hp.switch_driver_to_active_tab()

        lp = LoginPage(self.driver)
        # lp.refresh()
        lp.click_register_btn()

        rp = RegisterPage(self.driver)
        rp.verify_register_page_loaded_successfully(header_text)


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))