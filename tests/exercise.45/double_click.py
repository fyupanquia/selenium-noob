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
        
    def test_double_click(self):
        try:
            driver = self.driver
            driver.get('https://es.reactjs.org/')
            h1 = self.driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div/div/header/div/div/div/h1')
            actions = ActionChains(self.driver)
            actions.double_click(h1).perform()
            print('selected!!!!')
            time.sleep(3)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        verbosity=2)
