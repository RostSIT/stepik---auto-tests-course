selenium_env\Scripts\activate.bat
-----------------------------------
deactivate
====================================================================

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"


browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла

22.28588365215421
-------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

=============================================


from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
=====================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By

import math

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)
link = browser.find_element_by_link_text("224592")
link.click()

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text_redirect13.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(country)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




import math

str(math.ceil(math.pow(math.pi, math.e)*10000))

=====================================================

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_link_text_redirect13.html"


browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)
input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
time.sleep(1)
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Kum")
time.sleep(1)
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Kiev")
time.sleep(1)
input4 = browser.find_element_by_id("country")
input4.send_keys("UA")
time.sleep(1)
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)
browser.quit()


============================================================================
1.6 Поиск элементов с помощью Selenium WebDriver
6 из 13 шагов пройдено

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
    
elements = browser.find_elements_by_css_selector("input")
for element in elements:
       element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()


    # успеваем скопировать код за 30 секунд
time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла

===========================================================================
1.6 Поиск элементов с помощью Selenium WebDriver
6 из 13 шагов пройдено

from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
       element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
========================================================================================

# 1.6 Поиск элементов с помощью Selenium WebDriver
# 7 из 13 шагов пройдено

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")

input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")

input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")

input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

button = browser.find_element_by_xpath("//form/div[6]/button[3][@class='btn']")

# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
# ????????????????????????????????????????????????????
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 1.6 Поиск элементов с помощью Selenium WebDriver
# 10 из 13 шагов пройдено.

from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")

input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")

input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")

input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

button = browser.find_element_by_xpath("//form/div[6]/button[3][@class='btn']")

button.click()

    # успеваем скопировать код за 30 секунд
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()



================================================

#python c:\Users\OurComp\Desktop\tryFinally.py
#c:\Users\OurComp\get_method.py
# mkdir tryFinally
# copy C:\Users\OurComp\Desktop\tryfFinally.py c:\Users\OurComp\environments\tryFinally
# python c:\Users\OurComp\environments\tryFinally\tryfFinally.py




