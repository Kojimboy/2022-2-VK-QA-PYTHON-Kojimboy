from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from configuration.myapp_config import APP_SERVICE


class LoginPage(BasePage):
    locators = basic_locators.LoginPageLocators()
    url = f'http://{APP_SERVICE}:8080/login'

    def login(self, user, password):
        user_input = self.find(self.locators.USER_NAME_INPUT)
        user_input.clear()
        user_input.send_keys(user)

        pass_input = self.find(self.locators.PASSWORD_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)
        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()
        return BasePage(self.driver)
