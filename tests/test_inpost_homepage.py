from tests.base_test import BaseTestHome, BaseTestLogin
import unittest
import HtmlTestRunner


class HomePageTest(BaseTestHome):
    """
    Testy strony startowej inpost.pl
    """

    def test_home_page_loaded_successfully(self):
        """Test prawidłowego załadowania się strony domowej inpost.pl"""

        assert "InPost dla Ciebie" in self.driver.title


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
