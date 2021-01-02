import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Tables(unittest.TestCase):
    def setUp(self):
        """Start web driver"""
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        #self.driver = webdriver.Chrome(options=options, executable_path=r'../../chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=r'../../chromedriver.exe')

    def tearDow(self):
        """Stop web driver"""
        self.driver.quit()

    def test_sort_tables(self):
        driver = self.driver
        table_data = []
        try:
            """Find and click link with text Sortable Data Tables"""
            driver.get('https://the-internet.herokuapp.com/')
            driver.find_element_by_link_text('Sortable Data Tables').click()

            get_rows_table = driver.find_element_by_id('table1').get_property('rows')
            get_head_table = get_rows_table[0].get_property('cells')


            for i in range(1, len(get_rows_table)):
                data = {}
                for j in range(len(get_head_table)-1):
                    get_head_cells = get_head_table[j].text
                    get_body_cells = get_rows_table[i].get_property('cells')[j].text

                    data.update({get_head_cells:get_body_cells})
                table_data.append(data)

            print(table_data)


        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
