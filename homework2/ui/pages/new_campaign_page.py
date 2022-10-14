import time

import allure

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class NewCampaignPage(BasePage):
    locators = basic_locators.NewCampaignPageLocators()
    url = 'https://target-sandbox.my.com/campaign/new'

    def new_campaign(self):
        time.sleep(14)
        assert 1 ==1
        # assert self.find(self.locators.OBJECTIVE)
        # self.find(self.locators.OBJECTIVE).click()
        # time.sleep(10)
        # return CampaignPage(self.driver)
