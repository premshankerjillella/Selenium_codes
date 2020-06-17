from selenium import webdriver
import os

class RunChromeTests():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")

chromeTest = RunChromeTests()
chromeTest.test()
