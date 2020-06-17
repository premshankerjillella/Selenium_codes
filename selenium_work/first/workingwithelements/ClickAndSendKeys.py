from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver.get(baseUrl)
        driver.implicitly_wait(10) # This helps to wait so that code
        #runs so that all elements get loaded if it can't find in given time,
        # Then it fails

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID,"user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID,"user_password")
        passwordField.send_keys("test")

        time.sleep(3)
        emailField.clear()
        time.sleep(3)
        emailField.send_keys("Hi")
ct = ClickAndSendKeys()
ct.test()
time.sleep(2)
driver.close()