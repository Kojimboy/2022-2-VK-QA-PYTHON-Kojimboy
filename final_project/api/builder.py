from dataclasses import dataclass


class Builder:
    @staticmethod
    def user(name=None, surname=None, username=None, password=None, email=None, middlename=None):
        @dataclass
        class User:
            name: str
            surname: str
            username: str
            password: str
            email: str
            middlename: str
            id: None = None

        if name is None:
            name = "example_name"
        if surname is None:
            surname = "example_surname"
        if username is None:
            username = "ex"
        if password is None:
            password = "example_password"
        if email is None:
            email = "example_email"
        if middlename is None:
            middlename = ""

        return User(name=name, surname=surname, username=username, password=password,
                    email=email, middlename=middlename)
