from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators import HomePageLocators


class HomePage:
    """
    Strona domowa
    """

    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def close_covid_popup(self):
        try:
            covid_popup = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(HomePageLocators.COVID_POPUP_CLOSE_BTN))
            if covid_popup.is_visible() and covid_popup.is_enabled():
                covid_popup.click()
        except:
            print("popup is not visible")

    def click_sign_in_btn(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.LOG_IN_BTN)).click()

    def click_manager_paczek_btn(self):
        actions = ActionChains(self.driver)
        manager_paczek = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.MANAGER_BTN))
        actions.move_to_element(manager_paczek).perform()
        manager_paczek.click()

    def click_send_btn(self):
        actions = ActionChains(self.driver)
        send = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.SEND_BTN))
        actions.move_to_element(send).perform()

    def click_quick_send_btn(self):
        actions = ActionChains(self.driver)
        quick_send = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.QUICK_SEND_BTN))
        actions.move_to_element(quick_send).perform()
        quick_send.click()

    def switch_driver_to_active_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
