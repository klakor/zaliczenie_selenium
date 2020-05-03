from test_registration_incorrect_emails import RegistrationTestEmail
from test_registration_incorrect_names import RegistrationTestName
from test_registration_incorrect_passwords import RegistrationTestPassword
from test_registration_incorrect_phones import RegistrationTestPhone
from test_registration_incorrect_zipcodes import RegistrationTestZipcode
from test_registration_sending_empty_form import RegistrationTestEmptyForm
import unittest

class TestSuite(unittest.TestSuite):
    """
    Wszystkie testy strony Rejestracja
    """
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(RegistrationTestEmptyForm('test_empty_form'))
        suite.addTest(RegistrationTestEmail('test_incorrect_email'))
        suite.addTest(RegistrationTestName('test_registration_incorrect_names'))
        suite.addTest(RegistrationTestPassword('test_incorrect_password'))
        suite.addTest(RegistrationTestPhone('test_incorrect_phones'))
        suite.addTest(RegistrationTestZipcode('test_incorrect_zipcode'))
        return suite

if __name__ == "__main__":
  unittest.main()
