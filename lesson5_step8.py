from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

field = browser.find_element_by_id("answer").send_keys(y)
check = browser.find_element_by_id("robotCheckbox").click()
radio = browser.find_element_by_id("robotsRule").click()
button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(7)

browser.quit()
