import unittest

from ddt import ddt, data, unpack

from pages.inpost_home_page import HomePage
from pages.inpost_login_page import LoginPage
from tests.test_inpost_base import BaseTestLogin, BaseTestHome
from utils.inpost_utils import parse_expected_errors, get_data


class LoggingNavigationTest(BaseTestHome):
    def test_navigate_to_login_page(self):
        """Testing navigation from the home page to the login page"""
        header_text = "Zaloguj się do swojego konta"

        hp = HomePage(self.driver)
        # hp.close_covid_popup()
        hp.click_sign_in_btn()
        hp.click_manager_paczek_btn()
        hp.switch_driver_to_active_tab()

        lp = LoginPage(self.driver)
        # lp.refresh()
        lp.verify_login_page_loaded_successfully(header_text)


@ddt
class LoggingNegative(BaseTestLogin):
    """
    Testing the login page
    """
    @data(*get_data("data_logging_negative.csv"))
    @unpack
    def test_logging_negative(self, email, password, error):
        """Testing the new user's logging - negative"""
        expected_errors = parse_expected_errors(error)

        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.send_logging_form()
        lp.verify_is_logging_failed(expected_errors)


class LoggingPositive(BaseTestLogin):
    """
    Testing the login page
    """
    def test_logging_positive(self):
        """Testing the new user's logging - positive"""
        email = "cetojiy960@tmajre.com"
        password = "H@slo101"

        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.send_logging_form()
        lp.close_covid_popup()
        lp.verify_is_logging_succesfull(email)


if __name__ == "__main__":
    unittest.main(verbosity=1)
