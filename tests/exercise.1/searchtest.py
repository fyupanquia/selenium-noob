import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class SearchTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com")

	def test_search_tee(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		# clear field
		search_field.clear()

		# enter a value
		search_field.send_keys('tee')
		# send data
		search_field.submit()

	def test_search_salt_shaker(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')

		search_field.send_keys('salt shaker')
		search_field.submit()

		#searching by xpath
		products = driver.find_elements_by_xpath(
			'//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#compare
		self.assertEqual(1, len(products))

	def tearDown(self):
		self.driver.quit()
