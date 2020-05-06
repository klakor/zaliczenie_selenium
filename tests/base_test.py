import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("http://inpost.pl")
        self.driver.get("https://manager.paczkomaty.pl/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
