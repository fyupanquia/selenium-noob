import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class NoMessage(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe", options=chrome_options)
        self.driver.maximize_window()

    def test_no_message(self):
        try:
            driver = self.driver
            driver.get(
                "https://www.google.com")
            time.sleep(5)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
