import unittest
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

class DSelect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(
            'https://www.w3schools.com/howto/howto_custom_select.asp')
        iselect = driver.find_element_by_xpath(
            '//*[@id="main"]/div[3]/div[1]/select')
        options = iselect.find_elements_by_tag_name('option')
        for option in options:
            print('value: {0}, label: {1}'.format(option.get_attribute('value'), option.text))
            option.click()
            time.sleep(1)
        
        diselect = Select(iselect)
        diselect.select_by_value('11')
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
