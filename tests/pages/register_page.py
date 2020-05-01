from locators import RegisterPageLocators
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_email(self, email):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.EMAIL_INPUT)).send_keys(email)

    def fill_name(self, name):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(name)

    def fill_phone(self, phone):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.PHONE_INPUT)).send_keys(phone)

    def fill_zipcode(self, zipcode):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.ZIPCODE_INPUT)).send_keys(zipcode)

    def fill_password(self, password):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.PASSWORD_INPUT)).send_keys(password)

    def repeat_password(self, repeat_password):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(RegisterPageLocators.PASSWORD_REPEAT_INPUT)).send_keys(repeat_password)

    def fill_paczkomat(self, paczkomat):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.PACZKOMAT_INPUT)).send_keys(paczkomat)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(RegisterPageLocators.PACZKOMAT_INPUT)).send_keys(Keys.ENTER)

    def agree_to_newsletter(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.CHECKBOX_BTN)).click()

    def send_registration_form(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BTN)).click()

    def verify_errors(self, error):
        error_notices = self.driver.find_elements(*RegisterPageLocators.REGISTRATION_ERRORS)
        visible_errors = []
        for e in error_notices:
            if e.is_displayed():
                visible_errors.append(e.text)
        print("Visible error:")
        print(visible_errors)
        print("Error")
        print(error)
        assert visible_errors == error
        sleep(5)
