import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FindByHyperlink(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.w3schools.com/")
        href = driver.find_element_by_link_text('Learn AngularJS')
        print(href.click())
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
