from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_my_pets_have_different_names(driver_handler, go_to_my_pets):
    '''Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена'''
    
    element = WebDriverWait(driver_handler, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = driver_handler.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    
    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])
    
    # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
    # Проверяем, если r == 0 то повторяющихся имен нет.
    count = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            count += 1
    assert count == 0
    print("Количество совпадений:", count)
    print("Имена:", pets_name)