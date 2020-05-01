#from tests.base_test import BaseTest
from base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import unittest
import csv
from ddt import ddt, data, unpack

# pobieranie danych z pliku
def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    # Pomijam pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class RegistrationTest(BaseTest):
    """
    Testy strony Rejestracja
    """
    @data(*get_data("inpost_incorrect_emails.csv"))
    @unpack
    def test_incorrect_email(self, email, name, phone, zipcode, password, repeat_password, paczkomat, error):
        """Test rejestracji nowego użytkownika - błędny e-mail"""
        expected_errors = [error]
        if "|" in error:
            expected_errors = error.split("|")

        hp = HomePage(self.driver)
        hp.close_covid_popup()
        hp.click_sign_in_btn()
        hp.click_manager_paczek_btn()
        hp.switch_driver_to_active_tab()

        lp = LoginPage(self.driver)
        lp.click_register_btn()

        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_name(name)
        rp.fill_phone(phone)
        rp.fill_zipcode(zipcode)
        rp.fill_password(password)
        rp.repeat_password(repeat_password)
        rp.fill_paczkomat(paczkomat)
        rp.agree_to_newsletter()
        rp.send_registration_form()     # [ NIE STOSOWAĆ DLA PRZYPADKU POZYTYWNEGO !!!!]
        rp.verify_errors(expected_errors)

if __name__=="__main__":
    unittest.main(verbosity=1)
