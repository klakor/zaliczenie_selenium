import unittest

import HtmlTestRunner
from ddt import ddt, data, unpack

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from tests.base_test import BaseTestHome
from tests.base_test import BaseTestRegister
from utils.utils import parse_expected_errors, get_data


class RegistrationNavigationTest(BaseTestHome):
    def test_navigate_to_register_page(self):
        """
        Testing navigation from the home page to the register page
        """
        header_text = "Rejestracja"

        hp = HomePage(self.driver)
        # hp.close_covid_popup()        # popup showed at the beginning of the project
        hp.click_sign_in_btn()
        hp.click_manager_paczek_btn()
        hp.switch_driver_to_active_tab()

        lp = LoginPage(self.driver)
        lp.click_register_btn()

        rp = RegisterPage(self.driver)
        rp.verify_register_page_loaded_successfully(header_text)


@ddt
class RegistrationTest(BaseTestRegister):
    """
    Testing registration page
    """

    @data(*get_data("data_registration_negative.csv"))
    @unpack
    def test_registration_negative(self, email, name, phone, zipcode, password, repeat_password, boxmachine, error):
        """Testing registration of a new user - negative"""
        expected_errors = parse_expected_errors(error)

        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_name(name)
        rp.fill_phone(phone)
        rp.fill_zipcode(zipcode)
        rp.fill_password(password)
        rp.repeat_password(repeat_password)
        rp.fill_paczkomat(boxmachine)
        rp.agree_to_newsletter()
        rp.send_registration_form()
        rp.verify_errors(expected_errors)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
