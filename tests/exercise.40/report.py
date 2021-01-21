import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Report(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"../../chromedriver.exe")

    def test_taking_screenshot(self):

        try:
            driver = self.driver
            driver.get('https://http.cat/')
            cookies = driver.get_screenshot_as_file('./screenshot.png')
            time.sleep(3)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))
