from selenium.webdriver.common.by import By

class HomePageLocators():
    """ Selektory strony głównej"""
    COVID_POPUP = (By.XPATH, "//div[@id='popup-window']")
    COVID_POPUP_CLOSE_BTN = (By.XPATH, "//a[@id='popup-close']")
    LOGIN_BTN = (By.XPATH, "//button[@class='btn--primary -login']")
    MANAGER_BTN = (By.PARTIAL_LINK_TEXT, "Manager Paczek")

class LoginPageLocators():
    """ Slektory strony logowania"""
    REGISTRATION_BTN = (By.XPATH, "//a[@class='register']")

class RegisterPageLocators():
    """ Selektory strony Rejestracja"""
    EMAIL_INPUT = (By.XPATH, "//input[@id='input_email']")
    NAME_INPUT = (By.XPATH, "//input[@id='input_first_name']")
    PHONE_INPUT = (By.XPATH, "//input[@id='input_customer_telephone']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='input_postal_code']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_REPEAT_INPUT = (By.XPATH, "//input[@name='repeatPassword']")
    PACZKOMAT_INPUT = (By.XPATH, "//ng-select[@id='input_preferred_easypack']//input")
    CHECKBOX_BTN = (By.XPATH, "//input[@id='t3-newsletter']")
    REGISTER_BTN = (By.XPATH, "//button[@id='submit_submit']")
    REGISTRATION_ERRORS = (By.XPATH, "//ul[@class='errors']//li")
