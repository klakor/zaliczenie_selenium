import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Credentials:
c_email = (" ")
c_name = ("Anna")
c_phone = ("123456789")
c_zipCode = ("40645")
c_password = ("MojeHasl0!")
c_repeatPassword = ("MojeHasl0!")
#Wymagane jest od 8 do 16 znaków, w tym mała i duża litera, cyfra oraz znak specjalny (#?!@$%^&*-,).
c_paczkomat = ("KAT01A")


# Selectors:
s_popUp = ("//div[@id='popup-window']")
s_popUpClose = ("//a[@id='popup-close']")
s_logIn = ("//button[@class='btn--primary -login']")
s_manager = ("Manager Paczek")

s_registration = ("//a[@class='register']")

s_email = ("//input[@id='input_email']")
s_name = ("//input[@id='input_first_name']")
s_phone = ("//input[@id='input_customer_telephone']")
s_zipCode = ("//input[@id='input_postal_code']")
s_password = ("//input[@name='password']")
s_repeatPassword = ("//input[@name='repeatPassword']")
s_paczkomat = ("//ng-select[@id='input_preferred_easypack']//input")
s_checkbox = ("//input[@id='t3-newsletter']")
s_register = ("//button[@id='submit_submit']")


# Test scenario:
# Registration of a new account on http://inpost.pl

# Preconditions:
class InPostRegistration(unittest.TestCase):
    def setUp(self):
        # 1. Google Chrome browser is opened
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 2. http://inpost.pl is opened
        self.driver.get("http://inpost.pl")
        self.driver.implicitly_wait(15)

    # Test cases:
    # I. empty e-email field:
    def test_reg_empty_email(self):
        driver = self.driver
        actions = ActionChains(driver)
        # Steps:
        # 1. Close the pop-up window:
        sleep(5)
        if driver.find_elements_by_xpath(s_popUp):
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, s_popUpClose))).click()


        # 2. Find 'sign in' button and click it
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, s_logIn))).click()

        # 3. Find 'Manager Paczek' and click it
        managerPaczek = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, s_manager)))
        actions.move_to_element(managerPaczek).perform()
        managerPaczek.click()

        # 4. Switch driver to the active tab
        driver.window_handles
        driver.switch_to.window(driver.window_handles[1])

        # 5. Find 'Zarejestruj sie' and click it
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, s_registration))).click()

        # 6. Fill in the registration form
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_email))).send_keys(c_email)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_name))).send_keys(c_name)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_phone))).send_keys(c_phone)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_zipCode))).send_keys(c_zipCode)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_password))).send_keys(c_password)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_repeatPassword))).send_keys(c_repeatPassword)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_paczkomat))).send_keys(c_paczkomat)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, s_paczkomat))).send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, s_checkbox))).click()

        # 7. Find 'Zarejestruj sie' and click it
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, s_register))).click()

        errors = driver.find_elements_by_xpath("//ul[@class='errors']//li")
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e.text)

        assert visible_errors == ["Pole wymagane"]

        sleep(5)


    def tearDown(self):
        # Cleaning up
        # Shutting down the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=3)
