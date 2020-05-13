import os

from pages.home_page import HomePage
from tests.base_test import BaseTestQuickSend, BaseTestHome
from pages.quicksend_page import QuickSendPage
import unittest
import HtmlTestRunner
import csv
from ddt import ddt, data, unpack
from time import sleep

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


class NavigationTest(BaseTestHome):
    def test_navigate_to_quicksend_page(self):
        """Testing navigation from the home page to the quick send page"""
        header_pl = "Szybkie Nadania"
        header_ang = "Quick Send"
        hp = HomePage(self.driver)
        hp.click_send_btn()
        hp.click_quick_send_btn()
        hp.switch_driver_to_active_tab()

        qsp = QuickSendPage(self.driver)
        qsp.verify_quicksend_page_loaded_succesfully(header_pl, header_ang)
        sleep(5)

@ddt
class QuickSendNegative(BaseTestQuickSend):
    """
    Testing quick send page
    """

    @data(*get_data("data_quicksend_negative.csv"))
    @unpack
    def test_quicksend_negative(self, delivery, size, send_name, send_email, send_phone, send_boxmachine, rec_name, rec_email, rec_phone, rec_boxmachine, policy, error):
        """Testing quick send - negative"""
        expected_errors = [error]

        qsp = QuickSendPage(self.driver)
        qsp.language()
        qsp.choose_delivery(delivery)
        qsp.choose_size(size)
        qsp.fill_sender_name(send_name)
        qsp.fill_sender_email(send_email)
        qsp.fill_sender_phone(send_phone)
        qsp.fill_sender_boxmachine(send_boxmachine)
        qsp.fill_recipient_name(rec_name)
        qsp.fill_recipient_email(rec_email)
        qsp.fill_recipient_phone(rec_phone)
        qsp.fill_recipient_boxmachine(rec_boxmachine)
        qsp.accept_policy(policy)
        qsp.click_summary_btn()
        qsp.verify_errors(expected_errors)


if __name__ == "__main__":
    unittest.main(verbosity=3)