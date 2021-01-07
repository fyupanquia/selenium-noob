import unittest
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time


class RButton(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(
            "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        radio_bt1 = driver.find_element_by_xpath(
            "//*[@id='main']/div[3]/div[2]/label[1]/span")
        radio_bt2 = driver.find_element_by_xpath(
            "//*[@id='main']/div[3]/div[2]/label[2]/span")
        radio_bt2.click()
        time.sleep(1)
        radio_bt3 = driver.find_element_by_xpath(
            "//*[@id='main']/div[3]/div[2]/label[3]/span")
        radio_bt3.click()
        time.sleep(1)
        radio_bt4 = driver.find_element_by_xpath(
            "//*[@id='main']/div[3]/div[2]/label[4]/span")
        radio_bt4.click()
        time.sleep(1)
        radio_bt4.click()
        time.sleep(1)
        radio_bt3.click()
        time.sleep(1)
        radio_bt2.click()
        time.sleep(1)
        radio_bt1.click()
        time.sleep(1)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
