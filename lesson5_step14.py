from selenium import webdriver

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_id("button")