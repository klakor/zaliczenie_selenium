import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Variables:
first_name = "Stephen"
last_name = "Hawking"
invalid_passwd = "123"
valid_passwd = "123456"
invalid_email = "abcd"
duplicated_email = "testuser@mail.com"
unique_email = first_name.lower() + "." + last_name.lower() + "@mail.com"
valid_address = "London St."
valid_city = "Florida"
valid_zipcode = "10300"
valid_phone = "700500600"
valid_alias = "Home address"

# Test scenario:
# Registration of a new account on http://automationpractice.com/index.php

# Preconditions:
class APRegistration(unittest.TestCase):
    def setUp(self):
        # 1. Google Chrome browser is opened
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 2. http://automationpractice.com/index.php is opened
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(15)

    # Test cases:
    # I. empty e-email field:
    def test_reg_empty_email(self):
        driver = self.driver
        # Steps:
        # 1. Find 'sign in' button and click it
        signIn_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        signIn_button.click()

        # 2. Find 'create an account' button and click it
        createAccount_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon-user left']")))
        createAccount_button.click()
        #sleep(1)

        errors = driver.find_elements_by_xpath("//li[text()='Invalid email address.']")
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)

        assert len(visible_errors) == 1
        error_text = visible_errors[0].text
        assert error_text == "Invalid email address."
        print("Detected errors:")
        print(error_text)
        print(visible_errors)

    # II. Invalid e-email address
    def test_reg_invalid_email(self):
        driver = self.driver
        # Steps:
        # 1. Find 'sign in' button and click it
        signIn_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        signIn_button.click()

        # 2. Insert invalid e-mail address
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email_create']")))
        email_field.send_keys(invalid_email)

        # 3. Find 'create an account' button and click it
        createAccount_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon-user left']")))
        createAccount_button.click()
        #sleep(1)

        errors = driver.find_elements_by_xpath("//li[text()='Invalid email address.']")
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)

        assert len(visible_errors) == 1
        error_text = visible_errors[0].text
        assert error_text == "Invalid email address."
        print("Detected errors:")
        print(error_text)
        print(visible_errors)

    # III. Duplicated e-mail address: testuser@mail.com
    def test_reg_duplicated_email(self):
        driver = self.driver
        # Steps:
        # 1. Find 'sign in' button and click it
        signIn_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        signIn_button.click()

        # 2. Insert duplicated e-mail address
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email_create']")))
        email_field.send_keys(duplicated_email)

        # 3. Find 'create an account' button and click it
        createAccount_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon-user left']")))
        createAccount_button.click()
        #sleep(1)

        errors = driver.find_elements_by_xpath("//li[text()='An account using this email address has already been registered. Please enter a valid password or request a new one. ']")
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)

        assert len(visible_errors) == 1
        error_text = visible_errors[0].text
        assert error_text == "An account using this email address has already been registered. Please enter a valid password or request a new one."
        print("Detected errors:")
        print(error_text)
        print(visible_errors)

    # IV. Unique and valid e-email, empty field: first name
    #

    def test_reg_valid_email_no_first_name(self):
        driver = self.driver
        # Steps:
        # 1. Find 'sign in' button and click it
        signIn_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        signIn_button.click()

        # 2. Insert valid e-mail address
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email_create']")))
        email_field.send_keys(unique_email)

        # 3. Find 'create an account' button and click it
        createAccount_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon-user left']")))
        createAccount_button.click()
        #sleep(1)

        # 4. Find 'first name' field and leave it blank
        # first_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='customer_firstname']")))
        # first_name_field.send_keys(first_name)

        # 5. Find 'last name' field and complete it
        last_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='customer_lastname']")))
        last_name_field.send_keys(last_name)

        # 6. Check if an e-mail address is correct
        email_value = driver.find_element_by_xpath("//input[@id='email']").get_attribute("value")
        self.assertEqual(email_value, unique_email)

        # 7. Enter a password
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        password_field.send_keys(valid_passwd)

        # 8. Select a birth date
        day = Select(driver.find_element_by_xpath("//select[@id='days']"))
        day.select_by_value("21")
        month = Select(driver.find_element_by_xpath("//select[@id='months']"))
        month.select_by_value("7")
        year = Select(driver.find_element_by_xpath("//select[@id='years']"))
        year.select_by_value("1980")

        # 9. Enter an address
        address_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='address1']")))
        address_field.send_keys(valid_address)

        # 9. Enter the city name
        city_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='address1']")))
        city_field.send_keys(valid_city)

        # 10. Select a state
        state = Select(driver.find_element_by_xpath("//select[@id='id_state']"))
        state.select_by_value("9")

        # 11. Enter the zip code
        zipcode_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='postcode']")))
        zipcode_field.send_keys(valid_zipcode)

        # 12. Select a country
        valid_country = Select(driver.find_element_by_xpath("//select[@id='id_country']"))
        valid_country.select_by_value("21")

        # 13. Enter the mobile phone
        phone_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='phone_mobile']")))
        phone_field.send_keys(valid_phone)

        # 13. Enter an address alias
        alias_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='alias']")))
        alias_field.send_keys(valid_alias)

        # errors = driver.find_elements_by_xpath("//li[text()='An account using this email address has already been registered. Please enter a valid password or request a new one. ']")
        # visible_errors=[]
        # for e in errors:
        #     if e.is_displayed():
        #         visible_errors.append(e)
        #
        # assert len(visible_errors) == 1
        # error_text = visible_errors[0].text
        # assert error_text == "An account using this email address has already been registered. Please enter a valid password or request a new one."
        # print("Detected errors:")
        # print(error_text)
        # print(visible_errors)

    # V. Unique and valid e-email, empty field: last name
    #
    # VI. Unique and valid e-email, invalid password (too short)
    # VII. Unique and valid e-email, empty field: street name
    # VIII. Unique and valid e-email, empty field: city
    # IX. Unique and valid e-email, empty field: state
    # X. Unique and valid e-email, empty field: postal code
    # XI. Unique and valid e-email, invalid postal code: XX-XXX
    # XII. Unique and valid e-email, empty field: mobile phone
    # XIII. Unique and valid e-email, empty field: e-mail address alias
    # XIV. All fields completed corretcly


    def tearDown(self):
        # Cleaning up
        # Shutting down the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=1)
