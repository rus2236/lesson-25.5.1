def test_show_my_pets(driver_handler, go_to_my_pets):
    '''Проверяем что мы оказались на странице "Мои питомцы"'''

    assert driver_handler.current_url == 'https://petfriends.skillfactory.ru/my_pets'