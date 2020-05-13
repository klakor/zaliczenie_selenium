import os

from pages.home_page import HomePage
from tests.base_test import BaseTestLogin, BaseTestHome
from pages.login_page import LoginPage
import unittest
import csv
from ddt import ddt, data, unpack


# importing data from *csv file:
def get_data(file_name):
    rows = []
    data_file = open(os.path.join(os.path.dirname(__file__), file_name), 'rt')
    reader = csv.reader(data_file)
    # Skipping the first row:
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


class NavigationTest(BaseTestHome):
    def test_navigate_to_login_page(self):
        """Testing navigation from the home page to the login page"""
        header_text = ("Zaloguj się do swojego konta")

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
        expected_errors = [error]
        if "|" in error:
            expected_errors = error.split("|")

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
        email = ("cetojiy960@tmajre.com")
        password = ("H@slo101")

        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.send_logging_form()
        lp.close_covid_popup()
        lp.verify_is_logging_succesfull(email)


if __name__ == "__main__":
    unittest.main(verbosity=1)
