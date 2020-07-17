#1.6 Поиск элементов с помощью Selenium WebDriver
#10 из 13 шагов пройдено

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(3)
    browser.quit()


