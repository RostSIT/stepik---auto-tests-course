# 3.2.13 Задание оформляем тесты в стиле unittest. Тестирование web-приложений и тестовые фреймворки


from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(link)

import unittest

class TestLogs(unittest.TestCase):
    

input1 = browser.find_element_by_xpath("//form/div/div/input/.")
input1.send_keys("Ivan")
time.sleep(1)

input2 = browser.find_element_by_xpath("//form/div/div[2]/input/.")
input2.send_keys("Petrov")
time.sleep(1)

input3 = browser.find_element_by_xpath("//form/div/div[3]/input")
input3.send_keys("post-office@gmail.com")
time.sleep(1)

input4 = browser.find_element_by_xpath("//form/div[2]/div/input")
input4.send_keys("322-223-322")
time.sleep(1)

input5 = browser.find_element_by_xpath("//form/div[2]/div[2]/input")
input5.send_keys("Down house 2")
time.sleep(2)
button = browser.find_element_by_class_name("btn")

button.click()

    # успеваем скопировать код за 30 секунд
time.sleep(5)
    # закрываем браузер после всех манипуляций
browser.quit()
