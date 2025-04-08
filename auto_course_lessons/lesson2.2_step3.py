from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элементы, текст между тэгами, приводим к int вычисляем сумму
    x_element = browser.find_element(By.ID, 'num1')
    text_x = x_element.text
    x = int(text_x)
    y_element = browser.find_element(By.ID, 'num2')
    text_y = y_element.text
    y = int(text_y)
    summ = x + y
    
  #  x = int(browser.find_element(By.ID, 'num1').text.strip())
  #  y = int(browser.find_element(By.ID, 'num2').text.strip())    
    
    
    # Находим список на странице
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))  
    
    time.sleep(1)

    # находим кнопку Submit
    sb = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    sb.click()
    
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
