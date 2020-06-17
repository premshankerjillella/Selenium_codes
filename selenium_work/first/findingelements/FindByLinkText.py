from selenium import webdriver

class FindByLinkText():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_partial_link_text("Login")

        if elementByLinkText is not None:
            print("We found the element by Link Text")

        elementBypartialLinkText = driver.find_elements_by_partial_link_text("Pract")
        if elementBypartialLinkText is not None:
            print("Found the element by Partial Link Text")

ct = FindByLinkText()
ct.test()
