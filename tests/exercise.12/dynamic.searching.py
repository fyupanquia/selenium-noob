import csv
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

# get data from file
def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None) #omit header
    for row in reader:
        rows.append(row)

    return rows


@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../../chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    #getting data from external file
    @data(*get_data('testdata.csv'))
    @unpack #handle data such as individual item
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath(
            '//h2[@class= "product-name"]/a')
        lproducts =len(products)
        expected_count = int(expected_count)

        print(f"Found {lproducts} products for '{search_value}'")


        if expected_count > 0:
            self.assertEqual(expected_count, lproducts)
        else:
            message = driver.find_element_by_class_name('note-msg').text
            print(message,'<<<<<<')
            self.assertEqual('Your search returns no results.', message)
        
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
