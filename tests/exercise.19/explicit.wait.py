import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ExplicitWait(unittest.TestCase):
    
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
    cls.driver.maximize_window()

  def test_mercado_libre(self):
    name = "q"
    driver = self.driver
    driver.get('https://www.google.com/')

    try:
        el = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.NAME, name))
        )

        input_field = driver.find_element_by_name(name)
        input_field.send_keys('fyupanquia')
        time.sleep(3)

    finally:
       pass

  @classmethod
  def tearDownClass(cls):
    cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
