from selenium.webdriver.common.by import By


class HomePageLocators:
    """ Home page locators"""
    COVID_POPUP = (By.XPATH, "//div[@id='popup-window']")
    COVID_POPUP_CLOSE_BTN = (By.XPATH, "//a[@id='popup-close']")
    DANGER_ALERT_CLOSE_BTN = (By.XPATH, "//button[@class='close closeStatusMessageTrigger']")
    LOG_IN_BTN = (By.XPATH, "//button[@class='btn--primary -login']")
    MANAGER_BTN = (By.PARTIAL_LINK_TEXT, "Manager Paczek")
    SEND_BTN = (By.XPATH, "//ul[@class='main--menu mainMenu']//a[@title='Wysyłaj z InPost']")
    QUICK_SEND_BTN = (By.XPATH, "//ul[@class='submenu--list--desktop submenuListDesktop']//a[@title='Nadaj przesyłkę']")


class LoginPageLocators:
    """ Login page locators"""
    LOGGING_PAGE_HEADER = (By.XPATH, "//header[@class='mb-5']//h1")
    EMAIL_INPUT = (By.XPATH, "//input[@id='input_login']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='input_password']")
    LOG_IN_BTN = (By.XPATH, "//button[@id='submit_submit']")
    LOGGING_ERROR = (By.XPATH, "//ul[@class='errors']/li")
    ANTI_ROBOT_CHECKBOX = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    REGISTRATION_BTN = (By.XPATH, "//a[@class='register']")
    COVID_POPUP_CLOSE_BTN = (By.XPATH, "//div[@title='Koronawirus']/i")
    LOGGED_USER = (By.XPATH, "//span[@class='user-email p-1']")


class RegisterPageLocators:
    """ Register page locators"""
    HEADER = (By.XPATH, "//h1[@class='text-left pb-0 pt-0']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='input_email']")
    NAME_INPUT = (By.XPATH, "//input[@id='input_first_name']")
    PHONE_INPUT = (By.XPATH, "//input[@id='input_customer_telephone']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='input_postal_code']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_RPT_INPUT = (By.XPATH, "//input[@name='repeatPassword']")
    BOXMACHINE_INPUT = (By.XPATH, "//ng-select[@id='input_preferred_easypack']//input")
    BOXMACHINE_LIST = (By.XPATH, "//div[@class='scrollable-content']")
    ACCOUNT_TYPE_BTN = (By.XPATH, "//*[contains(text(),'Osoba fizyczna')]")
    CHECKBOX_BTN = (By.XPATH, "//input[@id='t3-newsletter']")
    REGISTER_BTN = (By.XPATH, "//button[@id='submit_submit']")
    REGISTRATION_ERRORS = (By.XPATH, "//ul[@class='errors']//li")


class QuickSendPageLocators:
    """Quick send page locators"""
    HEADER = (By.XPATH, "//h1[@class='page-title text-center']")
    LANGUAGE = (By.XPATH, "//div[@class='float-right lang']")
    DELIVERY_BOXMACHINE_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[1]")
    DELIVERY_ADDRESS_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[2]")
    PARCELSIZE_A_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[3]")
    PARCELSIZE_B_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[4]")
    PARCELSIZE_C_RADIO = (By.XPATH, "(//span[@class='input-checkmark'])[5]")
    SEND_NAME_INPUT = (By.XPATH, "//input[@placeholder='Wpisz imię i nazwisko lub nazwę firmy*']")
    SEND_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Wpisz adres e-mail*']")
    SEND_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Wpisz numer telefonu*']")
    SEND_BOXMACHINE_INPUT = (By.XPATH, "(//input[@role='combobox'])[1]")
    BOXMACHINE_LIST = (By.XPATH, "//div[@class='ng-option ng-option-marked']")
    REC_NAME_INPUT = (By.XPATH, "//input[@placeholder='Wpisz imię i nazwisko odbiorcy*']")
    REC_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Wpisz adres e-mail odbiorcy*']")
    REC_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Wpisz numer telefonu odbiorcy*']")
    REC_BOXMACHINE_INPUT = (By.XPATH, "(//input[@role='combobox'])[2]")
    SUMMARY_BTN = (By.XPATH, "//div[@id='parcelFormButton']//button")
    POLICY_CHECKBOX = (By.XPATH, "(//div[@class='input-checkmark'])[2]")
    SENDING_ERRORS = (By.XPATH, "//ul[@class='errors']")
