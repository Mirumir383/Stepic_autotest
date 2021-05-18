# -*- coding: utf8 -*-
from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    # calc(x)
    #button = browser.find_element_by_class_name("btn-primary")
    #browser.execute_script(
     # "return arguments[0].scrollIntoView(true);", button)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))
    #browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id('robotCheckbox').click()
    r = browser.find_element_by_id('robotsRule')    # находим robot rule
    browser.execute_script(
      "return arguments[0].scrollIntoView(true);", r)  # скролим до него
    r.click()                                           # кликаем
    butt = browser.find_element_by_class_name('btn-primary')
    butt.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()  