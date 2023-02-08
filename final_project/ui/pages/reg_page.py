import allure
from decouple import config

from ui.locators import page_locators
from ui.pages.base_page import BasePage
from configuration.myapp_config import APP_PORT


class RegPage(BasePage):
    locators = page_locators.RegPageLocators()
    url = f"http://{config('APP_SERVICE')}:{APP_PORT}/reg"

    @allure.step("sign_up form input filling and submitting")
    def sign_up(self, name, surname, username, email, password, middle_name=None):
        name_input = self.find(self.locators.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        surname_input = self.find(self.locators.SURNAME_INPUT)
        surname_input.clear()
        surname_input.send_keys(surname)

        if middle_name:
            middle_name_input = self.find(self.locators.MIDDLE_NAME_INPUT)
            middle_name_input.clear()
            middle_name_input.send_keys(middle_name)

        user_input = self.find(self.locators.USER_NAME_INPUT)
        user_input.clear()
        user_input.send_keys(username)
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.find(self.locators.PASSWORD_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)
        pass_confirm_input = self.find(self.locators.CONFIRM_PASSWORD_INPUT)
        pass_confirm_input.clear()
        pass_confirm_input.send_keys(password)

        terms = self.find(self.locators.TERM_CHECKBOX)
        terms.click()
        reg_button = self.find(self.locators.REGISTER_BUTTON)
        reg_button.click()
