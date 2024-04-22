#Webdriver - это и есть набор команд для управления браузером
from typing import Self
from selenium import webdriver

#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


import unittest
import time

link = "http://suninjuly.github.io/registration1.html"

class RegTestForm(unittest.TestCase):
    def test_registration_from_on_vilible(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            
            input_1 = browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your first name']")
            input_1.send_keys("Fox")
            input_2 = browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your last name']")
            input_2.send_keys("Patrikeevna")
            input_3 = browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your email']")
            input_3.send_keys("Fox@")
            input_4 = browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your phone:']")
            input_4.send_keys("+7963")
            input_5 = browser.find_element(By.CSS_SELECTOR,"[placeholder='Input your address:']")
            input_5.send_keys("Rossia")
          
        
            button = browser.find_element(By.CSS_SELECTOR,".btn-default")
            button.click()
            self.assertEqual(browser.find_element(By.TAG_NAME, 'h1').text, "Congratulations! You have successfully registered!",'No')
            # btn = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
            # btn.click()
            # h1_title = browser.find_element(By.TAG_NAME,'h1').text
            # print(h1_title)
            # self.assertEqual(h1_title,'Congratulations! You have successfully registered!')

        
        finally:
            time.sleep(30)
            browser.quit()
        
                


if __name__ == "__main__":
    unittest.main()