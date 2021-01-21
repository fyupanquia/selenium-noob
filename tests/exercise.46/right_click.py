import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time


class Assert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"../../chromedriver.exe")
        self.driver.maximize_window()
        
    def test_right_click(self):
        try:
            driver = self.driver
            driver.get('https://vuejs.org/')
            btn_github = self.driver.find_element_by_xpath(
                '//*[@id="hero"]/div/div[2]/p/a[3]')
            actions = ActionChains(self.driver)
            actions.context_click(btn_github).perform()
            print('right click showed!!!!')
            time.sleep(3)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
