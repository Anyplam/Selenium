#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver
#импортируем класс By , который позволяет выбрать способ поиска элемента
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
            browser.get("http://suninjuly.github.io/huge_form.html")
            element = browser.find_elements(By.TAG_NAME,'input')
            for i in element:
                i.send_keys("FOX")
            button = browser.find_element(By.TAG_NAME,'button')
            button.click()

        finally:
            time.sleep(5)
            browser.quit()

if __name__ == "__main__":
    unittest.main()