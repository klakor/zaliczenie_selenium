import os

from pages.register_page import RegisterPage
import unittest
import HtmlTestRunner
import csv
from ddt import ddt, data, unpack

# pobieranie danych z pliku
from tests.base_test import BaseTestRegister


def get_data(file_name):
    rows = []
    data_file = open(os.path.join(os.path.dirname(__file__), file_name), 'rt')
    reader = csv.reader(data_file)
    # Pomijam pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


@ddt
class RegistrationTest(BaseTestRegister):
    """
    Testy strony Rejestracja
    """

    @data(*get_data("incorrect_data.csv"))
    @unpack
    def test_registration(self, email, name, phone, zipcode, password, repeat_password, paczkomat, error):
        """Test rejestracji nowego użytkownika"""
        expected_errors = [error]
        if "|" in error:
            expected_errors = error.split("|")

        rp = RegisterPage(self.driver)
        rp.fill_email(email)
        rp.fill_name(name)
        rp.fill_phone(phone)
        rp.fill_zipcode(zipcode)
        rp.fill_password(password)
        rp.repeat_password(repeat_password)
        rp.fill_paczkomat(paczkomat)
        rp.agree_to_newsletter()
        rp.send_registration_form()  # [ NIE STOSOWAĆ DLA PRZYPADKU POZYTYWNEGO !!!!]
        rp.verify_errors(expected_errors)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
