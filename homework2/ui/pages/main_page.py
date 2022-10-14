import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class MainPage(BasePage):

    locators = basic_locators.MainPageLocators()
    url = 'https://target-sandbox.my.com/'

    def login(self, user, password):
        login_button = self.find(self.locators.LOGIN_FORM_BUTTON)
        login_button.click()
        assert "authForm-module-title" in self.driver.page_source
        login_input = self.find(self.locators.LOGIN_INPUT)
        login_input.clear()
        login_input.send_keys(user)
        pass_input = self.find(self.locators.PASSWORD_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)
        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()
        return BasePage(self.driver)

