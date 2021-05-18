# -*- coding: utf8 -*-
from selenium import webdriver
import time
import os

try:
    browser = webdriver.chrome()
    browser.get(' http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.alert.accept()
    x = browser.find_element_by_id('input_value')
    y = math.log(abs(12 * math.sin(int(x))))
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_class_name('btn-primary').click()

finally:
    time.sleep(7)
    browser.quit() 