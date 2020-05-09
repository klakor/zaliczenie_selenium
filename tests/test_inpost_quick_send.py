import os

from pages.register_page import RegisterPage
from tests.base_test import BaseTestHome
import unittest
import HtmlTestRunner
import csv
from ddt import ddt, data, unpack


class QuickSendTest(BaseTestHome):
    """
    Testy strony Rejestracja
    """
