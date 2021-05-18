# -*- coding: utf8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def calc(a, b):
  return int(a) + int(b)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    z = str(calc(x, y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    browser.find_element_by_class_name('btn-default').click()
    # Отправляем заполненную форму



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()