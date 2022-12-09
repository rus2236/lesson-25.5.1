from settings import valid_email, valid_password
from selenium.webdriver.common.by import By


def test_show_pet_friends(driver_handler):
    """Проверка карточек питомцев"""
    # Устанавливаем неявное ожидание
    driver_handler.implicitly_wait(3)

    # Вводим email
    driver_handler.find_element(By.ID, 'email').send_keys(valid_email)

    # Вводим пароль
    driver_handler.find_element(By.ID, 'pass').send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    driver_handler.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert driver_handler.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = driver_handler.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver_handler.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver_handler.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

