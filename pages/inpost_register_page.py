from inpost_locators import RegisterPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    """
    Register Page
    """
    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

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
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(RegisterPageLocators.PASSWORD_RPT_INPUT)).send_keys(repeat_password)

    def fill_paczkomat(self, boxmachine):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.BOXMACHINE_INPUT)).send_keys(boxmachine)
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.BOXMACHINE_LIST))
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.BOXMACHINE_INPUT)).send_keys(Keys.ENTER)

    def agree_to_newsletter(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.CHECKBOX_BTN)).click()

    def send_registration_form(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_BTN)).click()

    def verify_register_page_loaded_successfully(self, header_text):
        header = self.driver.find_element(*RegisterPageLocators.HEADER)
        if header.is_displayed():
            header = header.text.strip()
        assert header == header_text

    def verify_errors(self, error):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(RegisterPageLocators.REGISTRATION_ERRORS))
        error_notices = self.driver.find_elements(*RegisterPageLocators.REGISTRATION_ERRORS)
        visible_errors = []
        for e in error_notices:
            if e.is_displayed():
                visible_errors.append(e.text)
        assert visible_errors == error, "expected: " + error + ", actual: " + visible_errors
