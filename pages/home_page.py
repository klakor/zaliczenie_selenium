# import sys, os
# sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep
from locators import HomePageLocators


class HomePage:
    """
    Strona domowa
    """

    def __init__(self, driver):
        self.driver = driver

    def close_covid_popup(self):
        sleep(10)
        if self.driver.find_element(*HomePageLocators.COVID_POPUP):
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.COVID_POPUP_CLOSE_BTN)).click()

    def click_sign_in_btn(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.LOGIN_BTN)).click()

    def click_manager_paczek_btn(self):
        actions = ActionChains(self.driver)
        managerPaczek = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.MANAGER_BTN))
        actions.move_to_element(managerPaczek).perform()
        managerPaczek.click()

    def switch_driver_to_active_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
