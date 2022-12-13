import time
import allure
import pytest

from base import BaseCase
from ui.pages.base_page import BasePage


@pytest.mark.UI
class TestMainLinks(BaseCase):
    authorize = False

    @pytest.mark.Critical
    def test_valid_links(self, random_fields, reg_page):
        """
        Успешная регистрация: использует валидные значения из random_fields

        Шаги выполнения:
         1. Перейти на страницу регистрации
         2. заполнить поля Name, Surname, Username, Email, Password и Repeat password
         3. нажать на чекбокс для соглашения с условиями
         4. нажать на кнопку Register
         5. проверить что Username, Name и Surname правильно отображаются на главной странице

        Ожидаемый результат:
        Успешная регистрация и успешный вход на главную страницу под своим именем
        """
        base_page = reg_page.sign_up(*random_fields)
        self.logger.info('Assert success register ')
        assert self.driver.current_url == BasePage.url
        assert "Welcome!" in self.driver.title
        login, name_surname = base_page.get_user_login_names()
        assert random_fields[2] in login
        assert random_fields[0] and random_fields[1] in name_surname

