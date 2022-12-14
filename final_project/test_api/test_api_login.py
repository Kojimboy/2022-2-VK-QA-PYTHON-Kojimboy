import pytest


from base import ApiBase
from configuration.myapp_config import APP_SERVICE, APP_PORT


@pytest.mark.API
class TestApiLogin(ApiBase):
    @pytest.mark.Smoke
    def test_api_login(self, api_client):
        """
        Успешный логин с использованием api:

        Шаги выполнения:
         1. выполнить запрос на логин используя метод post_login
         2. проверить что вход выполнен сравнив url авторизованного и не авторизованного пользователя

        Ожидаемый результат:
        Успешный вход с помощью api
        """
        self.logger.info('Check success login with API')
        assert api_client.session.get(f"http://{APP_SERVICE}:{APP_PORT}/").url == \
               f"http://{APP_SERVICE}:{APP_PORT}/welcome/"

    @pytest.mark.Smoke
    def test_api_logout(self, api_client):
        """
        Успешный выход с использованием api:

        Шаги выполнения:
         1. выполнить запрос на логаут используя метод post_logaut
         2. проверить что выход выполнен сравнив url авторизованного и не авторизованного пользователя

        Ожидаемый результат:
        Успешный выход с помощью api
        """
        api_client.post_logout()
        self.logger.info('Check success logout with API')
        assert api_client.session.get(f"http://{APP_SERVICE}:{APP_PORT}/").url != \
               f"http://{APP_SERVICE}:{APP_PORT}/welcome/"
