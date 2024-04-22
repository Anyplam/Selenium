#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import time

def test_eception1():
    try:
        browser = webdriver.Chrome()
        browser.get('https://easysmarthub.ru/kak-ustanovit-selenium-webdriver-na-windows-i-zapustit-lokalnoe-okruzhenie-python-v-vs-code/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR,"[id = 'molodec']")
            pytest.fail('Element should not exist')


    finally:
        browser.quit()


def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get('https://easysmarthub.ru/kak-ustanovit-selenium-webdriver-na-windows-i-zapustit-lokalnoe-okruzhenie-python-v-vs-code/')
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR,"[id = 'molodec']")
            pytest.fail('Element should not exist')
    finally:
        browser.quit()