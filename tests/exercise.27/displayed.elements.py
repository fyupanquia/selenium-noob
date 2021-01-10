import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class HoverAction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.google.com/")
        btnI = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]')
        
        
        print("*"*5)
        print(btnI.is_enabled())
        print("*"*5)
        print(btnI.is_displayed())
        print("*"*5)
        print(btnI.get_attribute("value"))
        print("*"*5)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
