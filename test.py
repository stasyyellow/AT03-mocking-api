import pytest
from main import get_random_cat_image

# Тест для успешного запроса
def test_successful_cat_image_request(mocker):
    # Мокаем успешный ответ от API
    mock_response = [{
        "id": "c9g",
        "url": "https://cdn2.thecatapi.com/images/c9g.jpg",
        "width": 768,
        "height": 1024
    }]
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    # Проверяем, что функция возвращает правильный URL
    assert get_random_cat_image() == "https://cdn2.thecatapi.com/images/c9g.jpg"

# Тест для неуспешного запроса
def test_failed_cat_image_request(mocker):
    # Мокаем ответ с ошибкой (404)
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=404))

    # Проверяем, что функция возвращает None при неуспешном запросе
    assert get_random_cat_image() is None
