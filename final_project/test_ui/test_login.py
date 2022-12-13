import time
import allure
import pytest
from selenium.webdriver.common.by import By

from base import BaseCase
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


@pytest.mark.UI
class TestLogin(BaseCase):
    authorize = False

    # @pytest.mark.skip()
    @pytest.mark.Smoke
    def test_smoke_valid_login(self, credentials, login_page):
        """
        Тестирует успешный вход на главную страницу: использует валидные значения из credentials

        Шаги выполнения:
         1. Перейти на страницу авторизации
         2. заполнить поля Username и Password
         3. нажать кнопку Login
         4. проверить что Username отображается правильно на главной странице

        Ожидаемый результат:
        Успешный вход на главную страницу под своим именем
        """
        base_page = login_page.login(*credentials)
        self.logger.info('Check success login')
        assert "Welcome!" in self.driver.title
        login = base_page.get_user_login_names()
        assert credentials[0] in login[0]
        base_page.logout()
        time.sleep(10)

    @pytest.mark.skip()
    @pytest.mark.Smoke
    def test_smoke_invalid_login(self, credentials, login_page):
        base_page = login_page.login(*credentials)
        self.logger.info('Check error message')

