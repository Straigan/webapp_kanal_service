def test_home_page(test_client):
    """
    Проверка на открытие домашней страници сайта
    """
    response = test_client.get('/')
    assert response.status_code == 200