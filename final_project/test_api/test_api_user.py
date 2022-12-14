import pytest

from base import ApiBase


@pytest.mark.API
class TestApiUser(ApiBase):
    @pytest.mark.parametrize("name, surname, username, password, email, middlename", [
        ("Иван", "Иванов", "Ivanov", "SimplePassword", "AnotherEmail@mail.ru", "Николаев"),
    ],
                             ids=['Cirrilic_basic'])
    @pytest.mark.Smoke
    def test_api_add_user(self, user):
        """
        Добавление нового пользователя: использует валидные значения из parametrize

        Шаги выполнения:
         1. Выполнить запрос на логин используя метод post_login
         2. выполнить запрос на добавление пользователя используя метод post_user_create с значениями из parametrize
         3. проверить что пользователь появился в БД # еще не сделано

        Ожидаемый результат:
        Запрос выполнился и пользователь был добавлен в бд со своими параметрами
        """

        pass
        # проверить базу
        # assert self.add_user(user.name)
