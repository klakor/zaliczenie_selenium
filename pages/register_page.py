from locators import RegisterPageLocators
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


    # 6. Fill in the registration form
    def fill_email(self, name):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.EMAIL_INPUT)).send_keys(c_email)

    def fill_name(self, name):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.NAME_INPUT)).send_keys(c_name)

    def fill_phone(self, phone):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.PHONE_INPUT)).send_keys(c_phone)

    def fill_zipcode(self, code):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.ZIPCODE_INPUT)).send_keys(c_zipCode)

    def fill_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.PASSWORD_INPUT)).send_keys(c_password)

    def repeat_password(self, password2):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.PASSWORD_REPEAT_INPUT)).send_keys(c_repeatPassword)

    def fill_paczkomat(self, paczkomat):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.PACZKOMAT_INPUT)).send_keys(c_paczkomat)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(*RegisterPageLocators.PACZKOMAT_INPUT)).send_keys(Keys.ENTER)

    def agree_to_newsletter(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(*RegisterPageLocators.CHECKBOX_BTN)).click()

    def send_registration_form(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(*RegisterPageLocators.REGISTER_BTN)).click()

    def verify_errors(self, )
        errors = driver.find_elements(*RegisterPageLocators.REGISTRATION_ERRORS)
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e.text)

        assert visible_errors == ["Pole wymagane"]

        sleep(5)

def verify_visible_errors(self, number_of_errors, errors_texts):
    error_notices = self.driver.find_elements(*RegisterPageLocators.REGISTRATION_ERRORS)
    visible_error_notices = []
    # Zapisuję widoczne błędy do listy visible_error_notices
    for error in error_notices:
        if error.is_displayed():
            visible_error_notices.append(error)
    # Sprawdzam, czy widoczna jest właściwa liczba błędów
    assert len(visible_error_notices) == number_of_errors
    # Sprawdzam treść widocznych błędów
    errors_text_fact = []
    for i in range(len(visible_error_notices)):
        errors_text_fact.append(visible_error_notices[i].get_attribute("innerText") )
    print(errors_text_fact)
    print(errors_texts)
    assert errors_text_fact == errors_texts
