from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
class ZomatoTest():
	def test(self):
		baseUrl = "https://www.zomato.com/ncr"
		driver.implicitly_wait(10)
		driver.maximize_window()
		driver.get(baseUrl)

		location = driver.find_element(By.XPATH,"//input[@class='sc-krDsej gWvFwh']//parent::div//preceding-sibling::div//input")
		location.send_keys("Pune")
		location.click()
		item = driver.find_element(By.XPATH,"//div[@id='root']/div[3]/div[@class='contents-wrapper']/div[@class='searchContainer']/div/div[1]/div/div[1]/p[.='Pune']")
		item.click()
		time.sleep(2)

		cuisine = driver.find_element(By.XPATH,"//input[@class='sc-krDsej gWvFwh']")
		cuisine.send_keys("Pizza")
		cuisine.click()
		option = driver.find_element(By.XPATH,"//p[contains(text(),'Pizza - Delivery')]")
		time.sleep(2)
		option.click()
		time.sleep(2)
		#  No need for button to press when option directly selected
		# buttonToPress = driver.find_element(By.XPATH,"//div[@class='sc-fjmCvl eDkeYx']")
		# buttonToPress.click()
		rating = driver.find_element(By.XPATH,"//span[contains(text(),'Rating')]")
		rating.click()
		time.sleep(3)
		restraunt = driver.find_element(By.XPATH,"/html//div[@id='orig-search-list']/div[1]/div[@class='content']/div/article//a")
		restraunt.click()
		time.sleep(5)
		driver.back()
ct = ZomatoTest()
ct.test()
time.sleep(5)
