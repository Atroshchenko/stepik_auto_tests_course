from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click() 
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)    
    
    # Находим Х икс на странице и вычисляем по формуле
    x = browser.find_element(By.ID, 'input_value')
    number = x.text
    number = int(number)
    y = calc(number)  
    
    f = browser.find_element(By.ID, 'answer')
    f.send_keys(y)
    
    submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit.click() 
    
    time.sleep(2)
    
    confirm = browser.switch_to.alert
    confirm.accept()    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
