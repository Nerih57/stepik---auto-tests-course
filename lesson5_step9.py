from selenium import webdriver
import time
import math

def calc(u):
 return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

from selenium.webdriver.support.ui import Select

u = str
x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text
z = calc(u)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(z)

button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(7)

browser.quit()
