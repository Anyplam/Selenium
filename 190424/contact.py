#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver

#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import unittest
import time
import math

class RegTestForm(unittest.TestCase):
    1
    def test_registration_form_on_valible_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get('https://easysmarthub.ru/contact/')
            # button_click = browser.find_element(By.CLASS_NAME, '.gdpr-term')
            # button_click.click()
            button = browser.find_element(By.CSS_SELECTOR, 'button')
            button.click()
            time.sleep(10)
            button1 = browser.find_element(By.CSS_SELECTOR, '.wpcf7-response-output').text
            self.assertEqual(button1, 'В одном или нескольких полях указана ошибка. Пожалуйста, проверьте и повторите попытку')
        
        finally:
            time.sleep()
            browser.quit()


    # 2
    def test_registration_form_on_valid_2(self):
        try:
            browser = webdriver.Chrome()
            browser.get('https://easysmarthub.ru/contact/')
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("Fox")
            input_2 = browser.find_element(By.NAME, 'your-email')
            input_2.send_keys("Patrikeevna@mail.com")
            button = browser.find_element(By.CSS_SELECTOR, 'button')
            button.click()
            time.sleep(10)
            button2 = browser.find_element(By.CSS_SELECTOR, '.wpcf7-response-output').text
            self.assertEqual(button2, 'В одном или нескольких полях указана ошибка. Пожалуйста, проверьте и повторите попытку')
        
        finally:
            time.sleep()
            browser.quit()

    # 3  
    def test_registration_form_on_valible_3(self):
        try:
            browser = webdriver.Chrome()
            browser.get('https://easysmarthub.ru/contact/')
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("Fox")
            input_2 = browser.find_element(By.NAME, 'your-email')
            input_2.send_keys("DTFhjЛОЖпышре")
            button = browser.find_element(By.CSS_SELECTOR, 'button')
            button.click()
            time.sleep(10)
            button3 = browser.find_element(By.CSS_SELECTOR, '.wpcf7-response-output').text
            self.assertEqual(button3, 'В одном или нескольких полях указана ошибка. Пожалуйста, проверьте и повторите попытку')
        
        finally:
            time.sleep()
            browser.quit()



      # 4  
    def test_registration_form_on_valible_4(self):
        try:
            browser = webdriver.Chrome()
            browser.get('https://easysmarthub.ru/contact/')
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("Fox")
            input_2 = browser.find_element(By.NAME, 'your-email')
            input_2.send_keys("Patrikeevna@mail.com")
            input_3 = browser.find_element(By.NAME, 'your-subject')
            input_3.send_keys("Test")
            input_4 = browser.find_element(By.NAME, 'your-message')
            input_4.send_keys("Хочу домой")
            button = browser.find_element(By.CSS_SELECTOR, 'button')
            button.click()
            time.sleep(10)
            button4 = browser.find_element(By.CSS_SELECTOR, '.wpcf7-response-output').text
            self.assertEqual(button4, 'Вы должны принять правила и условия, прежде чем отправлять свое сообщение.')


        finally:
            time.sleep()
            browser.quit()


       # 5  
    def test_registration_form_on_valible_5(self):
        try:
            browser = webdriver.Chrome()
            browser.get('https://easysmarthub.ru/contact/')
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("Fox")
            input_2 = browser.find_element(By.NAME, 'your-email')
            input_2.send_keys("Patrikeevna@mail.com")
            input_3 = browser.find_element(By.NAME, 'your-subject')
            input_3.send_keys("Test")
            input_4 = browser.find_element(By.NAME, 'your-message')
            input_4.send_keys("Хочу домой")
            button_click = browser.find_element(By.CSS_SELECTOR, '.gdpr-term')
            button_click.click()
            button = browser.find_element(By.CSS_SELECTOR, 'button')
            button.click()
            time.sleep(10)
            button5 = browser.find_element(By.CSS_SELECTOR, '.wpcf7-response-output').text
            self.assertEqual(button5, 'Спасибо! Ваше сообщение успешно отправлено!')


        finally:
            time.sleep()
            browser.quit()

if __name__ == "__main__":
    unittest.main()