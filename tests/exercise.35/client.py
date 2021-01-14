import unittest
import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Client(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.sections()
        dchrome = config['Drivers']['chrome']
        self.config = config
        self.driver = webdriver.Chrome(executable_path=dchrome)
        #self.page = config['Pages']['google']

    def test_load_pages(self):
        
        try:
            config = self.config
            driver = self.driver
            
            for page in config['Pages']:
                print('Loading '+page)
                driver.get(config['Pages'][page])
                driver.implicitly_wait(5)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
