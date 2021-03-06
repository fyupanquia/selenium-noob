import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Client(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')

    def test_load_pages(self):

        try:
            driver = self.driver
            driver.get('https://http.cat/')
            driver.implicitly_wait(5)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
