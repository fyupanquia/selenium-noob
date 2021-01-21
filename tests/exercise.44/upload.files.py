import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import os

class Assert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()

    def test_upload_file(self):
        try:
            driver = self.driver
            driver.get(
                'https://s.bootsnipp.com/iframe/eNbOa')
            time.sleep(3)
            print(os.path.abspath("1.jpg"))
            btn_good_luck = self.driver.find_element_by_xpath(
                '//*[@id="imgInp"]').send_keys(os.path.abspath("1.jpg"))
            time.sleep(2)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
