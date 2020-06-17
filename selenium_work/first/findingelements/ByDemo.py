from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class ByDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID,"name")
        elementByXpath = driver.find_element(By.XPATH,"//input[@id='displayed-text']")
        elementByLinkText = driver.find_element(By.LINK_TEXT,"Login")

        if elementById is not None:
            print("Found element by Id")
        if elementByXpath is not None:
            print("Found element by Xpath")
        if elementByLinkText is not None:
            print('Found element by LinkText')

ct = ByDemo()
ct.test()