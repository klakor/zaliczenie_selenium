import unittest
from time import sleep

import HtmlTestRunner
from ddt import ddt, data, unpack

from pages.home_page import HomePage
from pages.quicksend_page import QuickSendPage
from tests.base_test import BaseTestQuickSend, BaseTestHome
from utils.utils import parse_expected_errors, get_data


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
        expected_errors = parse_expected_errors(error)

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
