import unittest
from selenium import webdriver

class ExplicitWait(unittest.TestCase):
    
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
    cls.driver.maximize_window()

  def test_mercado_libre(self):
    name = "q"
    driver = self.driver
    driver.implicitly_wait(5)
    driver.get('https://www.google.com/')

    input_field = driver.find_element_by_name(name)
    input_field.send_keys('fyupanquia')

  @classmethod
  def tearDownClass(cls):
    cls.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
