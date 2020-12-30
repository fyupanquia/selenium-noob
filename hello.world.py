import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_visit_twitter(self):
        driver = self.driver
        driver.get('https://twitter.com')

    def test_visit_facebook(self):
        driver = self.driver
        driver.get('https://www.facebook.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports',report_name='hello-word-report'))
        
