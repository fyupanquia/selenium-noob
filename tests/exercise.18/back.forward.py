import unittest
from selenium import webdriver
import time

class BackForward(unittest.TestCase):
    
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
    cls.driver.maximize_window()

  def test_mercado_libre(self):
    self.driver.get('https://www.youtube.com/')
    self.driver.get('https://stackoverflow.com/')
    self.driver.get('https://www.facebook.com/')
    time.sleep(2)
    self.driver.back()
    time.sleep(2)
    self.driver.back()
    time.sleep(2)
    self.driver.forward()
    time.sleep(2)
    self.driver.forward()

  @classmethod
  def tearDownClass(cls):
    cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
