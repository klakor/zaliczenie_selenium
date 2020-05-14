from selenium.webdriver import ActionChains

from locators import QuickSendPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class QuickSendPage:
    """
    Quick Send Page
    """
    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def language(self):
        header = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(QuickSendPageLocators.HEADER))
        language = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(QuickSendPageLocators.LANGUAGE))
        if "Quick Send" == header.text.strip():
            language.click()

    def choose_delivery(self, delivery):
        boxmachine = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.DELIVERY_BOXMACHINE_RADIO))
        address = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.DELIVERY_ADDRESS_RADIO))
        if delivery == "BOXMACHINE":
            boxmachine.click()
        elif delivery == "HOME":
            address.click()
        else:
            print("Delivery not selected, default delivery value")

    def choose_size(self, size):
        size_a = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.PARCELSIZE_A_RADIO))
        size_b = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.PARCELSIZE_B_RADIO))
        size_c = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.PARCELSIZE_C_RADIO))
        if size == "A":
            size_a.click()
        elif size == "B":
            size_b.click()
        elif size == "C":
            size_c.click()
        else:
            print("Size not selected")

    def fill_sender_name(self, send_name):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.SEND_NAME_INPUT)).send_keys(send_name)

    def fill_sender_email(self, send_email):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.SEND_EMAIL_INPUT)).send_keys(send_email)

    def fill_sender_phone(self, send_phone):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.SEND_PHONE_INPUT)).send_keys(send_phone)

    def fill_sender_boxmachine(self, send_boxmachine):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.SEND_BOXMACHINE_INPUT)).send_keys(send_boxmachine)
        sleep(2)
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(QuickSendPageLocators.BOXMACHINE_LIST))
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.SEND_BOXMACHINE_INPUT)).send_keys(Keys.ENTER)

    def fill_recipient_name(self, rec_name):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.REC_NAME_INPUT)).send_keys(rec_name)

    def fill_recipient_email(self, rec_email):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.REC_EMAIL_INPUT)).send_keys(rec_email)

    def fill_recipient_phone(self, rec_phone):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.REC_PHONE_INPUT)).send_keys(rec_phone)

    def fill_recipient_boxmachine(self, rec_boxmachine):
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.REC_BOXMACHINE_INPUT)).send_keys(rec_boxmachine)
        sleep(2)
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(QuickSendPageLocators.BOXMACHINE_LIST))
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.REC_BOXMACHINE_INPUT)).send_keys(Keys.ENTER)

    def accept_policy(self, policy):
        actions = ActionChains(self.driver)
        accept_policy = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(QuickSendPageLocators.POLICY_CHECKBOX))
        actions.move_to_element(accept_policy).perform()
        if policy == "YES":
            accept_policy.click()
        else:
            print("Policy terms checkbox not selected")

    def click_summary_btn(self):
        actions = ActionChains(self.driver)
        summary_btn = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(QuickSendPageLocators.SUMMARY_BTN))
        actions.move_to_element(summary_btn).perform()
        summary_btn.click()

    def verify_errors(self, error):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(QuickSendPageLocators.SENDING_ERRORS))
        error_notices = self.driver.find_elements(*QuickSendPageLocators.SENDING_ERRORS)
        visible_errors = []
        for e in error_notices:
            if e.is_displayed():
                visible_errors.append(e.text.replace("\n", " "))
        assert visible_errors == error, "expected: " + error + ", actual: " + visible_errors

    def verify_quicksend_page_loaded_succesfully(self, header_pl, header_ang):
        header = self.driver.find_element(*QuickSendPageLocators.HEADER)
        if header.is_displayed():
            header = header.text.strip()
        if header == header_pl:
            assert True
        elif header == header_ang:
            assert True
        else:
            assert False
