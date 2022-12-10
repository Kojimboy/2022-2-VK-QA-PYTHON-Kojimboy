import time
import allure
import pytest
from selenium.webdriver.common.by import By

from base import BaseCase
from ui.pages.login_page import LoginPage


@pytest.mark.UI
class TestLogin(BaseCase):
    @pytest.mark.parametrize("user, password", [("Lornuc", "Panda")
                                                ])  # логин и пароль
    # @pytest.mark.skip()
    @allure.step("Go to login page ")
    def test_valid_login(self, user, password):
        self.driver.get(LoginPage.url)
        login_page = LoginPage(self.driver)
        login = login_page.login(user, password)
        self.logger.info('Check success login')
        print(self.driver.title)
        assert "Welcome2!" in self.driver.title

    # def test_sel(self):
    #     # self.driver.get("http://localhost/login")
    #     self.driver.refresh()
    #     print(self.driver.find_element(By.XPATH, "/html/body").text)
    #     time.sleep(20)
    #     pass
