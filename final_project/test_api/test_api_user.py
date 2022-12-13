import pytest

from base import ApiBase


@pytest.mark.API
class TestApiUser(ApiBase):
    @pytest.mark.parametrize("name, surname, username, password, email, middlename", [
        ("Николай", "Николаевич", "Nickolas", "SimplePassword", "SimpleEmail@mail.ru", "Николаев"),
    ],
                             ids=['Cirrilic_basic'])
    @pytest.mark.Smoke
    def test_api_add_user(self, user):
        """
        Добавление нового пользователя: использует валидные значения из parametrize

        Шаги выполнения:
         1. Перейти на страницу регистрации
         2. заполнить поля Name, Surname, Middle name, Username, Email, Password и Repeat password
         3. нажать на чекбокс для соглашения с условиями
         4. нажать на кнопку Register
         5. проверить что Username, Name и Surname правильно отображаются на главной странице

        Ожидаемый результат:

        """

        pass
        # проверить базу
        # assert self.add_user(user.name)
