# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import math

driver = webdriver.Chrome()


#link = "http://suninjuly.github.io/registration2.html"
link ="http://suninjuly.github.io/registration.html"

driver.maximize_window()
driver.get(link)
pageLoadTimeOut = 20

try:
    # Ваш код, который заполняет обязательные поля

    first_name = driver.find_element_by_class_name("first")
    first_name.send_keys("blabla")

    last_name_label = driver.find_element_by_xpath("//label[text() = 'Last name*']")
    print last_name_label

    last_name = driver.find_element_by_class_name("second")
    last_name.send_keys("blabla")

    email = driver.find_element_by_class_name("third")
    email.send_keys("blabla")


    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
except Exception as ex:
    print ex
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(10)
    # закрываем браузер после всех манипуляций
    quit()


