import unittest
from selenium import webdriver
from openpyxl import load_workbook
from selenium.common.exceptions import WebDriverException
import time


class Exception(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()

    def test_exception(self):
        try:
            driver = self.driver
            driver.get(
                "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
            time.sleep(3)
            raise WebDriverException('This is a custom error')

        except WebDriverException as ex:
            print('Handled error:', ex.msg)
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
