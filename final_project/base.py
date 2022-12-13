import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from api.api_client import ResponseStatusCodeException
from api.builder import Builder
from mysql.mysql_client import MysqlClient


class BaseCase:
    driver = None
    authorize = True
    logger = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, api_client, mysql_client, request: FixtureRequest):  # на каждый запуск
        self.driver = driver
        self.config = config
        self.logger = logger

        self.api_client = api_client
        self.builder = Builder()

        self.client: MysqlClient = mysql_client

        if self.authorize:
            self.api_client.post_login()

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

    def get_methods(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TotalMethodsModel). \
            filter_by(**filters).order_by(TotalMethodsModel.count.desc()).all()


class ApiBase(BaseCase):
    authorize = True

    @pytest.fixture(scope='function')
    def user(self, name, surname, username, password, email, middlename):
        user_data = self.builder.user(name=name, surname=surname, username=username,
                                      password=password, email=email, middlename=middlename)
        user_add_response = self.add_user(name=user_data.name, surname=user_data.surname,
                                          username=user_data.username, password=user_data.password,
                                          email=user_data.email, middlename=user_data.middlename)
        # campaign_data.id = campaign_id

        yield user_data

        # self.delete_user(username=username)
        # assert self.check_active_top_campaign_id(campaign_id=campaign_id) is False

    def add_user(self, name, surname, username, password, email, middlename):
        # with pytest.raises(ResponseStatusCodeException):
        try:
            req = self.api_client.post_user_create(name=name, surname=surname,
                                                   username=username, password=password,
                                                   email=email, middlename=middlename)
            import pdb;
            pdb.set_trace()
            return req  # корректное сообщение проверить
        except ResponseStatusCodeException as exc:
            assert False, exc
