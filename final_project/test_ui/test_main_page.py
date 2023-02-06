import time
import allure
import pytest

from base import BaseCase
from ui.locators import page_locators


@pytest.mark.UI
@pytest.mark.skip()
class TestMainLinks(BaseCase):

    @pytest.mark.parametrize("locator_name, correct_url", [
        (page_locators.MainPageLocators.API_BUTTON, "https://en.wikipedia.org/wiki/API"),
        (page_locators.MainPageLocators.FUTURE_BUTTON, "https://www.popularmechanics.com/technology/infrastructure"
                                                       "/a29666802/future-of-the-internet/"),
        (page_locators.MainPageLocators.SMTP_BUTTON, "https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol")

    ], ids=['API', 'FUTURE', 'SMTP'])
    @pytest.mark.Smoke
    def test_valid_links(self, main_page, locator_name, correct_url):
        """
        Успешный переход по основным ссылкам: использует валидные значения из parametrize

        Шаги выполнения:
         1. Залогиниться и попасть на главную страницу
         2. нажать на ссылку
         3. проверить что ссылка открываетcя в новой вкладке и ведет на правильную страницу

        Ожидаемый результат:
        Ссылка открываетcя в новой вкладке и ведет на правильную страницу
        """
        current_window = self.driver.current_window_handle
        link_button = main_page.find(locator_name)
        link_button.click()
        self.logger.info('Assert success link ')
        assert len(self.driver.window_handles) > 1
        with self.switch_to_window(current=current_window, close=True):
            assert self.driver.current_url == correct_url, "wrong url"
