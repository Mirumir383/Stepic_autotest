# -*- coding: utf8 -*-
from selenium import webdriver
import time
import os
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# функция вычисления
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    

try:
    browser = webdriver.Chrome()
    browser.get(' http://suninjuly.github.io/explicit_wait2.html')
    # находим кнопку book
    button = browser.find_element_by_class_name('btn-primary') 
    # Ждем пока элемент прайс не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    # кликаем book
    button.click()
    # ищем значение Х . вычисляем . вносим в поле. кликаем кнопку
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_id('solve').click()
    # печатаем аллерт текст
    alert = browser.switch_to.alert
    print(alert.text)    
    
finally:
    time.sleep(15)
    browser.quit()