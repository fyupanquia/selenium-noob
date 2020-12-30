import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.maximize_window()
        driver.implicitly_wait(15)
     
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_count_or_promo_banner_imgs(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_vip_img_by_xpath(self):
        vip_promo = self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
    
    def test_shopping_car_by_css_selector(self):
        shopping_car_icon = self.driver.find_element_by_css_selector(
            'div.input-box button.search-button')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports',report_name='hello-word-report'))
        
