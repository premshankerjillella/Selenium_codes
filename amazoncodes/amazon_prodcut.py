import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--headless")
chrome_driver = os.getcwd() + "\\chromedriver.exe"    # This is for windows
# chrome_driver = os.getcwd()+'/chromedriver'   # This is for linux
driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
logging.basicConfig(filename='test.log', format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


class AmazonProduct():

    def selectProduct(self):
        baseUrl = "https://www.amazon.in"
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        searchBox = driver.find_element_by_id("twotabsearchtextbox")
        if searchBox is not None:
            logging.info("Search Box found")
        else:
            logging.error("Search Box Not Found")
        searchBox.send_keys("Earphones")
        driver.find_element(By.XPATH, "//input[ @type = 'submit' and @class ='nav-input']").click()
        rating_select = driver.find_element(By.XPATH, "//section[@aria-label='2 Stars & Up']")
        if rating_select is not None:
            logging.info("Rating element Found")
        else:
            logging.error("Rating element not found")

product = AmazonProduct()
product.selectProduct()
time.sleep(5)
driver.quit()
