#/usr/bin/env python3
import json
import os
import random
import requests
import time
import unittest
import warnings

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib3.exceptions import MaxRetryError

TIMEOUT=10


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        if os.environ.get('BROWSER') == 'chrome':
            browser = DesiredCapabilities.CHROME
        else:
            browser = DesiredCapabilities.FIREFOX
        while True:
            try:
                hub_status = requests.get('http://selenium-hub:4444/wd/hub/status')
            except:
                print('Waiting for selenium hub to become available...')
                time.sleep(1)
            else:
                if hub_status.json()['value']['ready']:
                    print('Hub is ready. Connecting...')
                    break
                else:
                    print('Waiting for nodes to be available...')
                    time.sleep(2)
        self.driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=browser)


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        wait = WebDriverWait(driver, TIMEOUT)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

