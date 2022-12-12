import time
import allure
import pytest

from base import BaseCase
from ui.pages.reg_page import RegPage
from ui.pages.base_page import BasePage


@pytest.mark.UI
class TestSignUp(BaseCase):
    authorize = False

    @pytest.mark.Smoke
    def test_smoke_valid_sign_up(self, random_fields, reg_page):
        base_page = reg_page.sign_up(*random_fields)
        self.logger.info('Assert success register ')
        assert self.driver.current_url == BasePage.url
        assert "Welcome!" in self.driver.title
        login, name_surname = base_page.get_user_login_names()
        assert random_fields[2] in login
        assert random_fields[0] and random_fields[1] in name_surname

    @pytest.mark.parametrize("locator_name, max_length, field_name", [
        (RegPage.locators.NAME_INPUT, 255, "Name"),
        (RegPage.locators.SURNAME_INPUT, 255, "Surname"),
        (RegPage.locators.MIDDLE_NAME_INPUT, 255, "Middle name"),
        (RegPage.locators.USER_NAME_INPUT, 16, "Username"),
        (RegPage.locators.EMAIL_INPUT, 64, "Email"),
        (RegPage.locators.PASSWORD_INPUT, 255, "Password"),
        (RegPage.locators.CONFIRM_PASSWORD_INPUT, 255, "Repeat password")
    ])
    @pytest.mark.Critical
    def test_sign_up_input_validation(self, locator_name, max_length, field_name, reg_page):
        el = reg_page.find(locator_name)

        self.logger.info('Get field attributes')
        attrs = []
        for attr in el.get_property('attributes'):
            attrs.append([attr['name'], attr['value']])

        attrs = dict(attrs)
        self.logger.info('Assert validation in fields')
        if not locator_name == RegPage.locators.MIDDLE_NAME_INPUT:
            assert "required" in attrs
        assert attrs.get("placeholder") == field_name
        assert int(attrs.get("maxlength")) <= max_length
        assert int(attrs.get("minlength")) >= 1

    @pytest.mark.parametrize("name, surname, middle_name, user_name, email, password", [
        ("Николай", "Николаевич", "Николаев", "Nickolas", "SimpleEmail@mail.ru", "SimplePassword"),
        ("Nicky", "Nickolaevich", "Nickolaev", "Nick-ol.as", "Not_soSimple.6@mail.ru",
         "Not_Simple!@#$%^&*()-_+=;:,./?|`{}Password"),
        ("12345678910", "12345678910", "12345678910", "12345678910", "123456@mail.ru", "12345678910"),
        ("Николай-николов.антонов", "Николаевич.Николов", "Николаев-николов", "NICKOLAS34", "CAPS_EMAIL@mail.ru",
         "PASSWORD23"),
        ("nickolas’vending", "nickolaevich’vending.gon", "Nick-olaev", "nickname-this", "new_email@mail.net",
         "passwordings$"),
    ],
        ids=['Cirrilic_basic', 'Latin_special', 'Numbers', 'Cirillic_Special', 'Latin-_special'])
    @pytest.mark.Critical
    def test_valid_sign_up(self, name, surname, middle_name, user_name, email, password, reg_page):
        base_page = reg_page.sign_up(name, surname, user_name, email, password, middle_name=middle_name)
        self.logger.info('Assert success register ')
        assert "Welcome!" in self.driver.title
        login, name_surname = base_page.get_user_login_names()
        assert user_name in login
        assert name and surname in name_surname
        # после тестов надо очистить базу

    @pytest.mark.Critical
    @pytest.mark.skip()
    @allure.step("Go to reg page ")
    def test_invalid_sign_up(self, name, surname, middle_name, user_name, email, password, reg_page):
        pass