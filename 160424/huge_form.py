#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import math
import os


try:
    
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    element = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    bcn = browser.find_element(By.CSS_SELECTOR, '[class ="btn btn-primary"]')
    bcn.click()
    time.sleep
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    x = browser.find_element(By.ID,'[id = "input_value"]')
    x = x.text
    input_blook = browser.find_element(By.ID,'[id ="answer"]')
    input_blook.send_keys(str(calc(x)))
    btn_2 = browser.find_element(By.ID,'solve')
    btn_2.click()
    


finally:
    time.sleep(10)
    browser.quit()
