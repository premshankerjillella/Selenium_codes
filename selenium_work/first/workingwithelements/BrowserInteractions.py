from selenium import webdriver

driver = webdriver.Chrome()
class BrowserInteractions():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"

        # window maximize
        driver.maximize_window()

        # Open the url
        driver.get(baseUrl)

        # Get title
        title = driver.title
        print(f"The title of the web page is {title}")

        # Get current Url
        currentUrl = driver.current_url
        print(f"The current Url is - {currentUrl}")

        # Browser Refresh
        driver.refresh()
        driver.get(driver.current_url)

        # Open another URl
        driver.get("https://www.google.com")

        # GO back
        driver.back()
        # go forward
        driver.forward()
        # get Page source
        pageSource = driver.page_source
        print(pageSource)
        # Browser close/quit
        driver.close()

ct = BrowserInteractions()
ct.test()