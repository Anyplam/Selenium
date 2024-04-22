#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver

#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import unittest
import time
import math


link = 'https://easysmarthub.ru/shop/'

class RegTestForm(unittest.TestCase):
    def test_registration_from_on_vilible(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            knig1 = browser.find_element(By.CSS_SELECTOR, '[data-product_id="1008"]')
            knig1.click()
            new_vklad = browser.find_element(By.CSS_SELECTOR,"[class='button wc-forward wp-element-button']")
            time.sleep(5)
            new_vklad.click()
            knig2 = browser.find_element(By.CSS_SELECTOR,'[data-product_id="1009"]')
            knig2.click()
            new_vklad1 = browser.find_element(By.CSS_SELECTOR,"[class='button wc-forward wp-element-button']")
            time.sleep(5)
            new_vklad1.click()
            knig3 = browser.find_element(By.CSS_SELECTOR,'[data-product_id="1011"]')
            knig3.click()
            oplat = browser.find_element(By.CSS_SELECTOR,'[href="https://easysmarthub.ru/checkout/"]')
            oplat.click()
            name = browser.find_element(By.ID,"billing_first_name")
            name.send_keys('Елена')
            fam = browser.find_element(By.ID,"billing_last_name")
            fam.send_keys('Крицкая')
            tel = browser.find_element(By.ID,"billing_phone")
            tel.send_keys('89633270000')
            mail = browser.find_element(By.ID,"billing_email")
            mail.send_keys('elenakricki@gmail.com')
            time.sleep(5)
            podtverdi = browser.find_element(By.CSS_SELECTOR,'place_order')
            podtverdi.click()
            input1 = browser.find_element(By.NAME,'card-number')
            input1.send_keys('5555555555554477')
            input2 = browser.find_element(By.NAME,'expiry-month')
            input2.send_keys('04')
            input3 = browser.find_element(By.NAME,'expiry-year')
            input3.send_keys('28')
            input4 = browser.find_element(By.NAME,'security-code')
            input4.send_keys('333')
            cart = browser.find_element(By.ID,'send-email-invoice')
            cart.click()
            pop = browser.find_element(By.CSS_SELECTOR,'button')
            pop.click()
            
            
        finally:
            time.sleep(5)
            browser.quit()
            
if __name__ == "__main__":
    unittest.main()