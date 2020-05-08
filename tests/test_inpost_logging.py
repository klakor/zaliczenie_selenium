import os
import sys

from tests.base_test import BaseTestLogin

sys.path.append("..")
from pages.login_page import LoginPage
import unittest
import csv
from ddt import ddt, data, unpack

# pobieranie danych z pliku
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
class LoggingNegative(BaseTestLogin):
    """
    Testy strony Logowanie
    """
    @data(*get_data("logging.csv"))
    @unpack
    def test_logging_negative(self, email, password, error):
        """Test logowania użytkownika zakończony porażką"""
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
    Testy strony Logowanie
    """
    def test_logging_positive(self):
        """Test logowania użytkownika zakończony pomyślnie"""
        email = ("cetojiy960@tmajre.com")
        password = ("H@slo101")

        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.send_logging_form()
        lp.close_covid_popup()
        lp.verify_is_logging_succesfull(email)


if __name__=="__main__":
    unittest.main(verbosity=1)
