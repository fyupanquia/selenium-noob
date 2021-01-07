import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

USERNAME = ''
PASSWORD = ''


class Gmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
        cls.driver.get('http://gmail.com')
        cls.driver.maximize_window()

    def test_enter_ufield(self):
        ufield =  self.driver.find_element_by_id('identifierId')
        ufield.send_keys(USERNAME)
        ufield.send_keys(Keys.ENTER)
        time.sleep(3)

    def test_enter_pfield(self):
        pfield = self.driver.find_element_by_name('password')
        pfield.send_keys(PASSWORD)
        ufield.send_keys(Keys.ENTER)
        time.sleep(3)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
