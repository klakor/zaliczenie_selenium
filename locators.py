from selenium.webdriver.common.by import By


class HomePageLocators():
    """ Selektory strony głównej"""
    COVID_POPUP = (By.XPATH, "//div[@id='popup-window']")
    COVID_POPUP_CLOSE_BTN = (By.XPATH, "//a[@id='popup-close']")
    LOG_IN_BTN = (By.XPATH, "//button[@class='btn--primary -login']")
    MANAGER_BTN = (By.PARTIAL_LINK_TEXT, "Manager Paczek")
    SEND_BTN = (By.XPATH, "//ul[@class='main--menu mainMenu']//a[@title='Wysyłaj z InPost']")
    QUICK_SEND_BTN = (By.XPATH, "//ul[@class='submenu--list--desktop submenuListDesktop']//a[@title='Nadaj przesyłkę']")


class LoginPageLocators():
    """ Selektory strony logowania"""
    LOGGING_PAGE_HEADER = (By.XPATH, "//div[@class='col-12 col-md-4 offset-md-2']/header/h1")
    EMAIL_INPUT = (By.XPATH, "//input[@id='input_login']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='input_password']")
    LOG_IN_BTN = (By.XPATH, "//button[@id='submit_submit']")
    LOGGING_ERROR = (By.XPATH, "//ul[@class='errors']/li")
    ANTI_ROBOT_CHECKBOX = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    REGISTRATION_BTN = (By.XPATH, "//a[@class='register']")
    COVID_POPUP_CLOSE_BTN = (By.XPATH, "//div[@title='Koronawirus']/i")
    LOGGED_USER = (By.XPATH, "//span[@class='user-email p-1']")
    LOGGING_ERROR = (By.XPATH, "//ul[@class='errors']/li")


class RegisterPageLocators():
    """ Selektory strony Rejestracja"""
    REGISTRATION_PAGE_HEADER = (By.XPATH, "//div[@class='col-12 col-sm-10 offset-sm-1']/header/h1")
    EMAIL_INPUT = (By.XPATH, "//input[@id='input_email']")
    NAME_INPUT = (By.XPATH, "//input[@id='input_first_name']")
    PHONE_INPUT = (By.XPATH, "//input[@id='input_customer_telephone']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='input_postal_code']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_REPEAT_INPUT = (By.XPATH, "//input[@name='repeatPassword']")
    PACZKOMAT_INPUT = (By.XPATH, "//ng-select[@id='input_preferred_easypack']//input")
    PACZKOMAT_LIST = (By.XPATH, "//div[@class='scrollable-content']")
    CHECKBOX_BTN = (By.XPATH, "//input[@id='t3-newsletter']")
    REGISTER_BTN = (By.XPATH, "//button[@id='submit_submit']")
    REGISTRATION_ERRORS = (By.XPATH, "//ul[@class='errors']//li")


class QuickSendPageLocators():
    """Selektory strony Szybkie Nadanie"""
    BOXMACHINE_RADIO = (By.XPATH, "//label[@for='deliveryTypeboxmachine']//i[@class='fa fa-circle']")
    ADDRESS_RADIO = (By.XPATH, "//label[@for='deliveryTypeaddress']//i[@class='fa fa-circle']")
    PARCELSIZE_A_RADIO = (By.XPATH, "//label[@for='parcelSizeA']//i[@class='fa fa-circle']")
    PARCELSIZE_B_RADIO = (By.XPATH, "//label[@for='parcelSizeB']//i[@class='fa fa-circle']")
    PARCELSIZE_C_RADIO = (By.XPATH, "//label[@for='parcelSizeC']//i[@class='fa fa-circle']")
    SEND_NAME_INPUT = (By.XPATH, "//input[@placeholder='Wpisz imię i nazwisko lub nazwę firmy*']")
    SEND_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Wpisz adres e-mail odbiorcy*']")
    SEND_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Wpisz numer telefonu odbiorcy*']")
    SEND_BOXMACHINE_INPUT = (By.XPATH, "//div[@class='ng-input']//input[@autocomplete='a1305a027b93']")
    REC_NAME_INPUT = (By.XPATH, "//input[@placeholder='Wpisz imię i nazwisko odbiorcy*']")
    REC_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Wpisz adres e-mail odbiorcy*']")
    REC_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Wpisz numer telefonu odbiorcy*']")
    REC_BOXMACHINE_INPUT = (By.XPATH, "//div[@class='ng-input']//input[@autocomplete='ad8eb4d95af9']")
    SUMMARY_BTN = (By.XPATH, "//button[@class='btn btn-submit position-relative with-loader']")
    POLICY_CHECKBOX = (By.XPATH, "//label[@for='terms']//i[@class='fa fa-check']")
