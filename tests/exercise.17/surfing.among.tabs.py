import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from surfer import Surfer

class SurfingTest(unittest.TestCase):
    
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
    cls.driver.maximize_window()

  def test_mercado_libre(self):
    s = Surfer(self.driver, sleep=2)
    s.addWebPage('https://www.youtube.com/')
    s.addWebPage('https://stackoverflow.com/')
    s.addWebPage('https://www.facebook.com/')

    s.surf()
    s.surf(1)
    s.surf(0)

    s.close()

  #@classmethod
  #def tearDownClass(cls):
  #  cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
