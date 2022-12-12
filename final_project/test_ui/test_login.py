import time
import allure
import pytest
from selenium.webdriver.common.by import By

from base import BaseCase
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


@pytest.mark.UI
class TestLogin(BaseCase):
    authorize = False

    # @pytest.mark.skip()
    @pytest.mark.Smoke
    def test_smoke_valid_login(self, credentials, login_page):
        base_page = login_page.login(*credentials)
        self.logger.info('Check success login')
        assert "Welcome!" in self.driver.title
        login = base_page.get_user_login_names()
        assert credentials[0] in login[0]
        base_page.logout()
        time.sleep(10)
        # после логина надо выходить


