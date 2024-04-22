from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import os


class TestEasysmarthub(unittest.TestCase):
    def test_1_all(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")           
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_submit.click()
            text1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))
            self.assertEqual("Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз.", text1.text, "should be equal")


        finally:
            browser.quit()


    def test_2_partially(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("test")
            input_2 = browser.find_element(By.NAME, 'your-email')
            input_2.send_keys("test")
            input_3 = browser.find_element(By.NAME, 'your-subject')
            input_3.send_keys("test")
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_submit.click()
            text1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))
            text2 = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'wpcf7-not-valid-tip')))
            self.assertEqual("Важно заполнить это поле.", text2.text, "should be equal")
            self.assertEqual("Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз.", text1.text, "should be equal")

        finally:
            browser.quit()

    def test_3_kartinka(self):
        try:
            file_path = r"C:\Users\AuroraPC\Desktop\Selenium\Selenium\photo-2023-11-08-150058.jpeg"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("test")
            input_3 = browser.find_element(By.NAME, 'your-subject')
            input_3.send_keys("test")
            input_jpg = browser.find_element(By.ID, 'kurs-zakonchilsya')
            input_jpg.send_keys(file_path)
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_submit.click()
            text1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))
            text2 = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'wpcf7-not-valid-tip')))
            self.assertEqual("Одно или несколько полей содержат ошибочные данные. Пожалуйста, проверьте их и попробуйте ещё раз.", text1.text, "should be equal")

        finally:
            browser.quit()    
            
            
    def test_4_pravil(self):
        try:
            file_path = r"C:\Users\AuroraPC\Desktop\Selenium\Selenium\photo-2023-11-08-150058.jpeg"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")
            input_1 = browser.find_element(By.NAME, 'your-name')
            input_1.send_keys("test")
            input_2 = browser.find_element(By.NAME, 'your-email')
            input_2.send_keys("test@nmd.ru")
            input_3 = browser.find_element(By.NAME, 'your-subject')
            input_3.send_keys("test")
            input_jpg = browser.find_element(By.ID, 'kurs-zakonchilsya')
            input_jpg.send_keys(file_path)
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_submit.click()
            text1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))
            self.assertEqual("Спасибо за Ваше сообщение. Оно успешно отправлено.", text1.text, "should be equal")

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()

