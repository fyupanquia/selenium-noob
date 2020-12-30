import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com")

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	def test_header(self):
		self.assertTrue(self.is_element_present(By.ID, 'header'))

	def tearDown(self):
		self.driver.quit()

	#how: type
	#what: value
	def is_element_present(self, how, what):
		try:  # busca los elementos según el parámetro
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as variable:
			return False
		return True
