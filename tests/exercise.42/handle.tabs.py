import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Assert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")

    def test_handle_tabs(self):
        try:
            driver = self.driver
            driver.get('https://www.google.com/intl/es-419/gmail/about/')
            time.sleep(2)
            btn_next = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]')
            btn_next.click()
            print(self.driver.current_window_handle)
            
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
                time.sleep(1)
            

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
