import unittest
from selenium import webdriver

class BaseTestHome(unittest.TestCase):
    """
    Klasa bazowa każdego testu rozpoczynającego się ze strony domowej
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://inpost.pl")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

class BaseTestLogin(unittest.TestCase):
    """
    Klasa bazowa każdego testu rozpoczynającego się ze strony logowania
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://manager.paczkomaty.pl/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()