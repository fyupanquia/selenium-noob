import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless") #No browser, background

class GRecommendation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'../../chromedriver.exe')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.google.com/")
        isearch = driver.find_element_by_name('q')
        search_word = 'seleni'
        isearch.send_keys(search_word)
        time.sleep(2)
        items = driver.find_elements_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li/div/div[2]/div[1]/span/b")
        for i, item in enumerate(items,0):
            print(f'result {i}: '+search_word+item.text)

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
