import time

import allure

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from configuration.myapp_config import APP_SERVICE, APP_PORT
from ui.locators import page_locators


class PageNotOpenedException(Exception):
    pass


class BasePage(object):  # logged
    locators = page_locators.BasePageLocators()
    url = f"http://{APP_SERVICE}:{APP_PORT}/welcome/"

    def is_opened(self, timeout=60):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 30
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

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

    # return LoginPage(self.driver) нужен майн page

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
