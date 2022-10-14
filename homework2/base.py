import os
from contextlib import contextmanager

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from ui.fixtures import get_driver
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.main_page import MainPage
from ui.pages.new_campaign_page import NewCampaignPage


class BaseCase:
    driver = None
    authorize = True

    # @contextmanager
    # def switch_to_window(self, current, close=False):
    #     for w in self.driver.window_handles:
    #         if w != current:
    #             self.driver.switch_to.window(w)
    #             break
    #     yield
    #     if close:
    #         self.driver.close()
    #     self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):  # на каждый запуск
        self.driver = driver
        self.config = config
        self.logger = logger

        self.main_page = MainPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.base_page = BasePage(driver)

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        # self.main_page: MainPage = (request.getfixturevalue('main_page'))
        # self.campaign_page: CampaignPage = (request.getfixturevalue('campaign_page'))
        # self.new_campaign_page: NewCampaignPage = (request.getfixturevalue('new_campaign_page'))

    @pytest.fixture(scope='session')
    def credentials(self):  # Берем почту и пароль с файла
        with open('creds.txt', 'r') as f:
            user = f.readline().strip()
            password = f.readline().strip()
        return user, password

    @pytest.fixture(scope='session')
    def cookies(self, credentials, config):
        driver = get_driver(config['browser'])
        driver.get(config['url'])
        driver.implicitly_wait(10)
        login_page = MainPage(driver)
        login_page.login(*credentials)
        cookies = driver.get_cookies()
        driver.quit()
        return cookies
