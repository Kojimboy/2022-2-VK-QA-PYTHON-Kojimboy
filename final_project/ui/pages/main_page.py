import allure

from ui.locators import page_locators
from ui.pages.base_page import BasePage
from configuration.myapp_config import APP_SERVICE, APP_PORT
from ui.pages.login_page import LoginPage


class MainPage(BasePage):  # logged
    locators = page_locators.MainPageLocators()
    url = f'http://{APP_SERVICE}:{APP_PORT}/welcome/'

    def __init__(self, driver):
        super().__init__(driver)
        assert "Welcome!" in self.driver.title

    @allure.step("get nickname and user name with surname from base page")
    def get_user_login_names(self):
        login = self.find(self.locators.NICKNAME).text
        username_surname = self.find(self.locators.NAME_SURNAME).text
        # распарсить нормально
        return login, username_surname

    @allure.step("logout from main page")
    def logout(self):
        logout_button = self.find(self.locators.LOGOUT_BUTTON)
        logout_button.click()
        return LoginPage(self.driver)  # нужен майн page
