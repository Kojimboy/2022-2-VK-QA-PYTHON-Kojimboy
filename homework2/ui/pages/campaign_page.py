import time

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class CampaignPage(BasePage):
    locators = basic_locators.CampaignPageLocators()
    url = 'https://target-sandbox.my.com/campaigns'

    def checking(self):
        self.driver.get(CampaignPage.url)
        assert self.find(self.locators.OBJECTIVE)
        self.find(self.locators.OBJECTIVE).click()
        time.sleep(10)
        return CampaignPage(self.driver)


