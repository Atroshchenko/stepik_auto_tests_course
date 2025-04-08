from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Jopa')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Popa')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('popa_jopa@jopa.com')
    
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'jopa.txt')
    
    button = browser.find_element(By.ID, 'file')
    button.send_keys(file_path)
    
    submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    