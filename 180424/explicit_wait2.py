#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver

#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import unittest
import pytest
import os

class RegTestForm(unittest.TestCase):
    def test_registration_form_on_valible(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("http://suninjuly.github.io/explicit_wait2.html")
            element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
            btn = browser.find_element(By.ID, 'book')
            btn.click()
            def calc(x):
                return str(math.log(abs(12*math.sin(x))))
            x = browser.find_element(By.ID,'input_value')
            x = int(x.text)
            input_block = browser.find_element(By.ID,'answer')
            input_block.send_keys(calc(x))
            btn_2 = browser.find_element(By.ID,'solve')
            btn_2.click()

        finally:
            time.sleep(5)
            browser.quit()

if __name__ == '__main__':
    unittest.main()