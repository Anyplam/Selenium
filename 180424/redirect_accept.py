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
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/redirect_accept.html")
            btn = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
            btn.click()
            window_page = browser.window_handles[1]
            browser.switch_to.window(window_page)
            math_element = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]')
            x = int(math_element.text)
            input_form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
            input_form.send_keys(calc(x))
            button = browser.find_element(By.TAG_NAME, 'button')
            button.click()
        finally:
            time.sleep(10)
            browser.quit()
            
if __name__ == "__main__":
    unittest.main()