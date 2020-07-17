# 3.2.13 Задание оформляем тесты в стиле unittest. Тестирование web-приложений и тестовые фреймворки


from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block .first")  # xpath("//form/div/div/input/.") - замнил после поправки проверяющего, не уникальный селектор, 5 вар.
        input1.send_keys("Ivan")
        time.sleep(1)
        input2 = browser.find_element_by_css_selector(".first_block .second")  # //form/div/div[2]/input/. - замнил после поправки проверяющего, не уникальный селектор, 2 вар.
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
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_class_name("container")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be text...")
        time.sleep(5)
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block .first") # xpath("//form/div/div/input/.") - замнил после поправки проверяющего, не уникальный селектор, 5 вар.
        input1.send_keys("Ivan")
        time.sleep(1)
        input2 = browser.find_element_by_css_selector(".first_block .second") # //form/div/div[2]/input/. - замнил после поправки проверяющего, не уникальный селектор, 2 вар.
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
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_class_name("container")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be text...")
        time.sleep(5)
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()
# последняя строка
