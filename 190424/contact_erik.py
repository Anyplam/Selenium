from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class TestEasysmarthub(unittest.TestCase):
    def test_1_all(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://easysmarthub.ru/contact/")           
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_submit.click()
            text1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))
            self.assertEqual("В одном или нескольких полях указана ошибка. Пожалуйста, проверьте и повторите попытку", text1.text, "should be equal")


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
            checkbox = browser.find_element(By.NAME, 'gdpr')
            checkbox.click()
            button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
            button_submit.click()
            text1 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output")))
            text2 = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'wpcf7-not-valid-tip')))
            self.assertEqual("The e-mail address entered is invalid.", text2.text, "should be equal")

        finally:
           
            browser.quit()





if __name__ == "__main__":
    unittest.main()



