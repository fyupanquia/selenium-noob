import time

class Surfer(object):

    def __init__(self, driver, sleep):
        self._driver = driver
        self._webpages = []
        self._sleep = sleep

    def addWebPage(self, url):
        self._webpages.append(url)

    def surf(self, index=None):

        if index!=None:
           self._driver.switch_to.window(self._driver.window_handles[index])
           time.sleep(self._sleep)
           return True

        for i, wb in enumerate(self._webpages, start=1):
            self._driver.get(self._webpages[i-1])
            time.sleep(self._sleep)
            if i<len(self._webpages):
                self._driver.execute_script("window.open('')")
                self._driver.switch_to.window(self._driver.window_handles[i])

    def close(self):
        for i, wb in enumerate(self._webpages, start=1):
            self._driver.switch_to.window(self._driver.window_handles[0])
            self._driver.close();
        
