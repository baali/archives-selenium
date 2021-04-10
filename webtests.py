#/usr/bin/env python3
import os
import time
import unittest
import warnings

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from urllib3.exceptions import MaxRetryError

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        if os.environ.get('BROWSER') == 'chrome':
            browser = DesiredCapabilities.CHROME
        else:
            browser = DesiredCapabilities.FIREFOX
        while True:
            try:
                self.driver = webdriver.Remote(
                    command_executor='http://selenium-hub:4444/wd/hub',
                    desired_capabilities=browser
                )
            except (WebDriverException, MaxRetryError):
                print('Waiting for selenium hub to become available...')
                time.sleep(0.2)
            else:
                print('Connected to the selenium hub.....')
                break

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

