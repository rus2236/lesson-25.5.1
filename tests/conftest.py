import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def driver_handler():
   return webdriver.Chrome('/chromedriver.exe')

@pytest.fixture(autouse=True)
def browser_handler(driver_handler):
   driver_handler.set_window_size(1024, 768)
   # Переходим на страницу авторизации
   driver_handler.get('https://petfriends.skillfactory.ru/login')
   yield
   driver_handler.quit()

@pytest.fixture()
def go_to_my_pets(driver_handler):
   element = WebDriverWait(driver_handler, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   driver_handler.find_element(By.ID, "email").send_keys(valid_email)

   element = WebDriverWait(driver_handler, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   driver_handler.find_element(By.ID, "pass").send_keys(valid_password)

   element = WebDriverWait(driver_handler, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
   # Нажимаем на кнопку входа в аккаунт
   driver_handler.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

   element = WebDriverWait(driver_handler, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   driver_handler.find_element(By.LINK_TEXT, "Мои питомцы").click()


   