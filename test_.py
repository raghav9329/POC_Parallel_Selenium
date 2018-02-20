from selenium import webdriver
from junit_xml import TestSuite, TestCase
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time, unittest

class OnInternetExplorer (unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Remote(
        command_executor='http://172.17.0.3:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    def test_Google_Search_IE(self):
        driver = self.driver
        driver.get("http://www.google.com")
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys("testing")
        inputElement.submit()
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
