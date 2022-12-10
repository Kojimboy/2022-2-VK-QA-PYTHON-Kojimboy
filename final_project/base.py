import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


class BaseCase:
    driver = None
    authorize = True
    logger = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):  # на каждый запуск
        self.driver = driver
        self.config = config
        self.logger = logger

        # self.base_page = BasePage(driver)

        # if self.authorize:
        #     cookies = request.getfixturevalue('cookies')
        #     for cookie in cookies:
        #         self.driver.add_cookie(cookie)
        #     self.driver.refresh()
        #     self.base_page = BasePage(driver)

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            test_logs = os.path.join(temp_dir, 'test.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'browser.log', allure.attachment_type.TEXT)
            with open(test_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)
