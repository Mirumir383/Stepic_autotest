# -*- coding: utf8 -*-
from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element_by_name('firstname').send_keys('Vasya')
    browser.find_element_by_name('lastname').send_keys('Пупкин')
    browser.find_element_by_name('email').send_keys('Vasya@klmn.ru')
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    # находим кноаку загрузить файл, посылаем туда путь к файлу
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_class_name('btn-primary').click() #жмем submit
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()      
    


