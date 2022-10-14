import time

import allure

from base import BaseCase
from ui.locators import basic_locators
from ui.pages.main_page import MainPage


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        login_page = MainPage(self.driver)

        login_page.login("*credentials", "dsf")
        # self.logger.info("asserting что все так")
        # assert self.main_page.find(basic_locators.BasePageLocators.AUTHORIZED_USER_RIGHT_MODULE)
        time.sleep(15)


# class TestLK(BaseCase):
#
#     def test_lk1(self):
#         time.sleep(3)
#
#     def test_lk2(self):
#         time.sleep(3)
