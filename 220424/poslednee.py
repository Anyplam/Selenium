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
            kod = browser.find_element(By.CSS_SELECTOR,'[class="input-text form-control"]')
            kod.send_keys('ERIK_CAT')
            cli = browser.find_element(By.CSS_SELECTOR,'[name="apply_coupon"]')
            cli.click
            time.sleep(10)
            oplat = browser.find_element(By.CSS_SELECTOR,'[href="https://easysmarthub.ru/checkout/"]')
            oplat.click()
            time.sleep(5)
            podtverdi = browser.find_element(By.CSS_SELECTOR,'.place_order')
            podtverdi.click()
            
        finally:
            time.sleep(5)
            browser.quit()
            
if __name__ == "__main__":
    unittest.main()