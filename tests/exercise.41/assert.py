import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Assert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")

    def test_title_equal(self):
        try:
            driver = self.driver
            driver.get('https://http.cat/')
            title = driver.title
            self.assertEqual('HTTP Gatos', title, 'Something wrong with the page title')
            time.sleep(3)
        except NoSuchElementException as ex:
            self.fail(ex.msg)
    
    def test_title_not_equal(self):
        try:
            driver = self.driver
            driver.get('https://http.cat/')
            title = driver.title
            self.assertNotEqual('HTTP Cats', title,
                             'Something wrong with the page title')
            time.sleep(3)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
