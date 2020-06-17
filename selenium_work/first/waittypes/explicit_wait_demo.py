from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=options)
class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.expedia.co.in"
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        flights_section = driver.find_element(By.ID,"tab-flight-tab-hp")
        flights_section.click()

        origin = driver.find_element(By.ID,"flight-origin-hp-flight")
        origin.send_keys("SFO")

        destination = driver.find_element(By.ID,"flight-destination-hp-flight")
        destination.send_keys("NYC")

        driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("06/12/2020")
        returnDate = driver.find_element(By.ID,"flight-returning-hp-flight")
        returnDate.clear()
        returnDate.send_keys("08/12/2020")

        driver.find_element(By.XPATH,"//button[@class='btn-primary btn-action gcw-submit']").click()
        wait = WebDriverWait(driver,10,poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
        element.click()
ct = ExplicitWaitDemo()
ct.test()