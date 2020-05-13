import unittest

import HtmlTestRunner

from tests.base_test import BaseTestHome


class HomePageTest(BaseTestHome):
    """
    Testing home page - inpost.pl
    """

    def test_home_page_loaded_successfully(self):
        """Testing if the home page inpost.pl is loaded succesfully"""

        assert "InPost dla Ciebie" in self.driver.title


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
