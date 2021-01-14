import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Client(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie(executable_path=r'../../IEDriverServer.exe')

    def test_load_pages(self):

        try:
            driver = self.driver
            driver.get('https://http.cat/')
            time.sleep(3)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
