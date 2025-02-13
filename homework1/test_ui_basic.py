import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base import BaseCase
from ui.locators import basic_locators


@pytest.mark.parametrize("registered_email, valid_password", [("mr-nicko2011@Yandex.ru", "Test_password123!"),
                                                              ])
@pytest.mark.UI
class TestValidLogin(BaseCase):
    def test_valid_login(self, registered_email, valid_password):
        assert "myTarget" in self.driver.title
        self.login(registered_email, valid_password)
        assert self.find(*basic_locators.AUTHORIZED_USER_RIGHT_MODULE)


@pytest.mark.UI
class TestInvalidLogin(BaseCase):
    @pytest.mark.parametrize("invalid_email, invalid_password", [("123mail.ru", "1234"),
                                                                 ("sFVAsd", "dfsdf")])
    def test_invalid_login(self, invalid_email, invalid_password):
        assert "myTarget" in self.driver.title
        self.login(invalid_email, invalid_password)
        assert self.find(*basic_locators.INVALID_INPUT_ERROR_MESSAGE)

    @pytest.mark.parametrize("unregistered_email, password", [("123@mail.ru", "Test_pass1234!"),
                                                              ("SDFdsd@mail.ru", "dfsdf")])
    def test_unregister_user_login(self, unregistered_email, password):
        assert "myTarget" in self.driver.title
        self.login(unregistered_email, password)
        assert self.find(*basic_locators.INVALID_LOGIN_PASSWORD_ERROR_MESSAGE)


@pytest.mark.parametrize("registered_email, valid_password", [("mr-nicko2011@Yandex.ru", "Test_password123!"),
                                                              ])
@pytest.mark.UI
class TestLoggedInUser(BaseCase):
    def test_logout(self, registered_email, valid_password):
        assert "myTarget" in self.driver.title
        self.login(registered_email, valid_password)
        self.logout()
        assert self.find(*basic_locators.LOGIN_LOCATOR)

    @pytest.mark.parametrize("fio, phone_number", [("Иван Иванович", "+71234867890"),
                                                   ])
    def test_edit_user_info(self, registered_email, valid_password, fio, phone_number):
        assert "myTarget" in self.driver.title
        self.login(registered_email, valid_password)
        self.edit_profile(fio, phone_number)
        success_message = self.find(*basic_locators.EDIT_SUCCESS_MESSAGE)
        assert WebDriverWait(self, 5).until(EC.visibility_of(success_message))  # проверка появления сообщения об
        # успешном сохранении изменении
        self.driver.refresh()
        updated_user_name = self.find(*basic_locators.AUTHORIZED_USER_NAME_IN_RIGHT_MODULE)
        assert updated_user_name.get_attribute("title") == fio

    @pytest.mark.parametrize("locator, assert_locator",
                             [(basic_locators.AUDITIONS_BUTTON, basic_locators.AUDITIONS_ASSERT_LOCATOR),
                              (basic_locators.BILLING_BUTTON, basic_locators.BILLING_ASSERT_LOCATOR),
                              ])
    def test_page_transition(self, registered_email, valid_password, locator, assert_locator):
        assert "myTarget" in self.driver.title
        self.login(registered_email, valid_password)
        self.change_page(locator)
        assert self.find(*assert_locator)
