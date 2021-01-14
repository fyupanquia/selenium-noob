import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class CSSSelector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.w3schools.com/")
        href = driver.find_element_by_css_selector(
            '#main > div.w3-row.w3-margin-bottom > div.w3-col.l6.w3-center > a:nth-child(3)')
        print(href.click())
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)