from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим Х икс на странице и вычисляем по формуле
    x_image = browser.find_element(By.ID, 'treasure')
    x = x_image.get_attribute('valuex')
    y = calc(x)  
    
    # Находим поле для ввода ответа, чекбокс, радиобаттон
    f = browser.find_element(By.ID, 'answer')
    f.send_keys(y)
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    time.sleep(3)

    # находим кнопку Submit
    sb = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    sb.click()
    
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
