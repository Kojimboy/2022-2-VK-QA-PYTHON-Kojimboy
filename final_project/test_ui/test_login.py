import time

import pytest

from base import BaseCase
from ui.pages.main_page import MainPage


@pytest.mark.UI
class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.Smoke
    def test_smoke_valid_login(self, credentials, login_page):
        """
        Тестирует успешный вход на главную страницу: использует валидные значения из credentials

        Шаги выполнения:
         1. Перейти на страницу авторизации
         2. заполнить поля Username, Password и нажать на кнопку Login
         3. проверить что Username отображается правильно на главной странице

        Ожидаемый результат:
        Успешный вход на главную страницу под своим именем
        """
        login_page.login(*credentials)
        main_page = MainPage(self.driver)
        self.logger.info('Check success login')
        login = main_page.get_user_login_names()
        assert credentials[0] in login[0]

    @pytest.mark.skip()
    @pytest.mark.Smoke
    def test_smoke_invalid_login(self, credentials, login_page):
        login_page.login(*credentials)
        self.logger.info('Check error message')
