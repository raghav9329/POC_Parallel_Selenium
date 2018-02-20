from selenium import webdriver
from junit_xml import TestSuite, TestCase
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest

class Chrome1(unittest.TestCase):

    def setUp(self) :
        self.driver = webdriver.Remote(
        command_executor='http://172.17.0.2:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    def test_Google_Search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        inputElement = driver.find_element_by_name("dsd")
        inputElement.send_keys("Cheese!")
        inputElement.submit()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
