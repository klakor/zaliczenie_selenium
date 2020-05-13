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
    HEADER = (By.XPATH, "//div[@class='col-12 col-sm-10 offset-sm-1']/header/h1")
    EMAIL_INPUT = (By.XPATH, "//input[@id='input_email']")
    NAME_INPUT = (By.XPATH, "//input[@id='input_first_name']")
    PHONE_INPUT = (By.XPATH, "//input[@id='input_customer_telephone']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='input_postal_code']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_RPT_INPUT = (By.XPATH, "//input[@name='repeatPassword']")
    BOXMACHINE_INPUT = (By.XPATH, "//ng-select[@id='input_preferred_easypack']//input")
    BOXMACHINE_LIST = (By.XPATH, "//div[@class='scrollable-content']")
    CHECKBOX_BTN = (By.XPATH, "//input[@id='t3-newsletter']")
    REGISTER_BTN = (By.XPATH, "//button[@id='submit_submit']")
    REGISTRATION_ERRORS = (By.XPATH, "//ul[@class='errors']//li")


class QuickSendPageLocators():
    """Selektory strony Szybkie Nadanie"""
    HEADER = (By.XPATH, "//h1[@class='page-title text-center']")
    LANGUAGE = (By.XPATH, "//div[@class='float-right lang']")
    DELIVERY_BOXMACHINE_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[1]")
    DELIVERY_ADDRESS_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[2]")
    PARCELSIZE_A_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[3]")
    PARCELSIZE_B_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[4]")
    PARCELSIZE_C_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[5]")
    SEND_NAME_INPUT = (By.XPATH, "//input[@placeholder='Wpisz imię i nazwisko lub nazwę firmy*']")
    SEND_EMAIL_INPUT = (By.XPATH, "//*[@id='parcelForm']/div/div[1]/app-dynamic-form/form/app-section[3]/div/div/app-input[3]/div/div/app-input-text/input")
    SEND_PHONE_INPUT = (By.XPATH, "//*[@id='parcelForm']/div/div[1]/app-dynamic-form/form/app-section[3]/div/div/app-input[4]/div/div/app-input-text/input")
    SEND_BOXMACHINE_INPUT = (By.XPATH, "//*[@id='parcelForm']/div/div[1]/app-dynamic-form/form/app-section[3]/div/div/app-input[13]/div/div/app-points-select/ng-select/div/div/div[2]/input")
    BOXMACHINE_LIST = (By.XPATH, "//div[@class='ng-option ng-option-marked']")
    REC_NAME_INPUT = (By.XPATH, "//input[@placeholder='Wpisz imię i nazwisko odbiorcy*']")
    REC_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Wpisz adres e-mail odbiorcy*']")
    REC_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Wpisz numer telefonu odbiorcy*']")
    REC_BOXMACHINE_INPUT = (By.XPATH, "//*[@id='parcelForm']/div/div[1]/app-dynamic-form/form/app-section[4]/div/div/app-input[5]/div/div/app-points-select/ng-select/div/div/div[2]/input")
    SUMMARY_BTN = (By.XPATH, "//div[@id='parcelFormButton']//button")
    POLICY_CHECKBOX = (By.XPATH, "(//div[@class='input-checkmark'])[2]")
    SENDING_ERRORS = (By.XPATH, "//ul[@class='errors']")
