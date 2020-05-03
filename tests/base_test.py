import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://inpost.pl")
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)

    def tearDown(self):
        self.driver.quit()
