import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class HoverAction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.google.com/")
        time.sleep(3)
        el = driver.find_element_by_link_text("Privacidad")
        hover = ActionChains(driver).move_to_element(el)
        hover.perform()
        time.sleep(3)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
