from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # говорим Selenium проверять в течение 12 секунд, 
  # пока кнопка цена станет 100
  rent = WebDriverWait(browser, 12).until(
         EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
  button = browser.find_element(By.ID, 'book')
  button.click()
  
  # Находим Х икс на странице и вычисляем по формуле
  x = browser.find_element(By.ID, 'input_value')
  number = x.text
  number = int(number)
  y = calc(number) 
  
  f = browser.find_element(By.ID, 'answer')
  f.send_keys(y)  

  button_2 = browser.find_element(By.ID, 'solve')
  button_2.click()
  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()  
