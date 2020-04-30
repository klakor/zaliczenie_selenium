from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_register_btn(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(LoginPageLocators.REGISTRATION_BTN)).click()

    def click_register_by_facebook(self):
        pass
