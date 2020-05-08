from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def fill_email(self, email):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)

    def fill_password(self, password):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)).send_keys(password)

    def send_logging_form(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.LOG_IN_BTN)).click()

    def close_covid_popup(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.COVID_POPUP_CLOSE_BTN)).click()

    def verify_login_page_loaded_successfully(self, header_text):
        header = self.driver.find_element(*LoginPageLocators.LOGGING_PAGE_HEADER)
        if header.is_displayed():
            header = header.text.strip()
        assert header == header_text

    def verify_is_logging_succesfull(self, email):
        username = self.driver.find_element(*LoginPageLocators.LOGGED_USER)
        if username.is_displayed():
            visible_username = username.text.strip()
        assert visible_username == email

    def verify_is_logging_failed(self, error):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.LOGGING_ERROR))
        error_notices = self.driver.find_elements(*LoginPageLocators.LOGGING_ERROR)
        visible_errors = []
        for e in error_notices:
            if e.is_displayed():
                visible_errors.append(e.text)
        print('error ze strony ', visible_errors)
        print('error z testu', error)
        assert visible_errors == error

    def click_log_in_by_allegro(self):
        pass

    def click_log_in_by_facebook(self):
        pass

    def click_register_btn(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(LoginPageLocators.REGISTRATION_BTN)).click()

    def click_register_by_facebook(self):
        pass
