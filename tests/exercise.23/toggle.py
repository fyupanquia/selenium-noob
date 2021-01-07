import unittest
from selenium import webdriver
import time


class Toggle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        name = "q"
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get('https://www.w3schools.com/howto/howto_css_switch.asp')
        toggle = driver.find_element_by_xpath('//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(2)
        toggle.click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
