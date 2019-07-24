from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(7)
browser.get(link)

RUR = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )

button = browser.find_element_by_css_selector("button.btn")
button.click()
	
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

field = browser.find_element_by_id("answer")
field.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()

time.sleep(17)

browser.quit()
