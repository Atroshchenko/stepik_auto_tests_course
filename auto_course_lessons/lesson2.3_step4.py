from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click() 
    
    confirm = browser.switch_to.alert
    confirm.accept()    
    
    # Находим Х икс на странице и вычисляем по формуле
    x = browser.find_element(By.ID, 'input_value')
    number = x.text
    number = int(number)
    y = calc(number)  
    
    f = browser.find_element(By.ID, 'answer')
    f.send_keys(y)
    
    submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit.click()    

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
