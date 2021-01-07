import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Gmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
        cls.driver.get('https://www.google.com/')
        cls.driver.maximize_window()
        cls.qfield = None

    def test_enter_ufield(self):
        self.qfield = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        time.sleep(2)
        self.qfield.send_keys('fyupanquia', Keys.ARROW_DOWN)
        time.sleep(2)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
