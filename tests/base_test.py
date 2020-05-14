import unittest

from selenium import webdriver


class BaseTestHome(unittest.TestCase):
    """
    Base class of every test initialized on home page
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
    Base class of every test initialized on login page
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://manager.paczkomaty.pl/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()


class BaseTestRegister(unittest.TestCase):
    """
    KBase class of every test initialized on register page
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://manager.paczkomaty.pl/auth/register")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()


class BaseTestQuickSend(unittest.TestCase):
    """
    Base class of every test initialized on quick send page
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://inpost.pl/SzybkieNadania/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
