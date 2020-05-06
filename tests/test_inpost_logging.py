import sys
sys.path.append("..")
from base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import unittest
import HtmlTestRunner
from time import sleep
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
class LoggingTestNegative(BaseTest):
    """
    Testy strony Logowanie
    """
    @data(*get_data("logging.csv"))
    @unpack
    def test_logging_negative_empty_password(self, email, password, error):
        """Test logowania użytkownika zakończony porażką"""
        expected_errors = [error]
        if "|" in error:
            expected_errors = error.split("|")

        lp = LoginPage(self.driver)
        lp.fill_email(email)
        lp.fill_password(password)
        lp.send_logging_form()
        lp.verify_is_logging_failed(error)


# class LoggingTestPositive(BaseTest):
#     """
#     Testy strony Logowanie
#     """
#     def test_logging_positive(self):
#         """Test logowania użytkownika zakończony pomyślnie"""
#         email = ("cetojiy960@tmajre.com")
#         password = ("H@slo101")
#
#         lp = LoginPage(self.driver)
#         lp.fill_email(email)
#         lp.fill_password(password)
#         lp.send_logging_form()
#         lp.close_covid_popup()
#         lp.verify_is_logging_succesfull(email)


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
