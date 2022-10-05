import pytest
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import basic_locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, by, what):
        try:
            return self.driver.find_element(by, what)
        except NoSuchElementException:
            assert False, f"No element found with locator {what}"

    def login(self, email, password):
        login_button = self.find(*basic_locators.LOGIN_LOCATOR)
        login_button.click()
        assert "authForm-module-title" in self.driver.page_source
        login_input = self.find(*basic_locators.LOGIN_INPUT)
        login_input.clear()
        login_input.send_keys(email)
        pass_input = self.find(*basic_locators.PASSWORD_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)
        login_button = self.find(*basic_locators.LOGIN_BUTTON)
        login_button.click()

    def logout(self):
        right_module_wrap = self.find(*basic_locators.AUTORIZED_USER_RIGHT_MODULE)
        right_module_wrap.click()
        logout_button = self.find(*basic_locators.LOGOUT_BUTTON)
        right_drop_menu = self.find(*basic_locators.RIGHT_DROP_MENU)
        try:
            WebDriverWait(self, 5).until(
                EC.element_to_be_clickable(right_drop_menu))
            logout_button.click()
        except StaleElementReferenceException:
            right_module_wrap = self.find(*basic_locators.AUTORIZED_USER_RIGHT_MODULE)
            right_module_wrap.click()
            logout_button = self.find(*basic_locators.LOGOUT_BUTTON)
            right_drop_menu = self.find(*basic_locators.RIGHT_DROP_MENU)
            WebDriverWait(self, 5).until(
                EC.element_to_be_clickable(right_drop_menu))  # Ждем пока можно будет кликнуть на кнопку логаута
            logout_button.click()

    def edit_profile(self, fio, phone_number):
        profile_button = self.find(*basic_locators.EDIT_PROFILE_BUTTON)
        try:
            profile_button.click()
        except StaleElementReferenceException:
            profile_button = self.find(*basic_locators.EDIT_PROFILE_BUTTON)
            profile_button.click()
        fio_input = self.find(*basic_locators.EDIT_FIO_INPUT)
        fio_input.clear()
        fio_input.send_keys(fio)
        phone_input = self.find(*basic_locators.EDIT_PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone_number)
        save_button = self.find(*basic_locators.EDIT_SAVE_BUTTON)
        save_button.click()

    def change_page(self, locator):
        button = self.find(*locator)
        try:
            button.click()
        except StaleElementReferenceException:
            button = self.find(*locator)
            button.click()
