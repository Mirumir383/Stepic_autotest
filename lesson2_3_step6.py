# -*- coding: utf8 -*-
from selenium import webdriver
import time
import os
import math
try:
    browser = webdriver.Chrome()
    browser.get(' http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_class_name('btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    print(x)
    y = math.log(abs(12 * math.sin(int(x))))
    print(y)
    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_class_name('btn-primary').click()

finally:
    time.sleep(7)
    browser.quit()