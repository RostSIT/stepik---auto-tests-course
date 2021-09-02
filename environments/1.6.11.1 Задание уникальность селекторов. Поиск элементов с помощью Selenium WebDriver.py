#1.6.11.1 Задание уникальность селекторов. Поиск элементов с помощью Selenium WebDriver

# №1.

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//form/div/div/input/.")
    input1.send_keys("Ivan")
    time.sleep(0.5)
    input2 = browser.find_element_by_xpath("//form/div/div[2]/input/.")
    input2.send_keys("Ohlobystin")
    time.sleep(0.5)
    input3 = browser.find_element_by_xpath("//form/div/div[3]/input")
    input3.send_keys("post-office@gmail.com")
    time.sleep(0.5)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(0.5)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

