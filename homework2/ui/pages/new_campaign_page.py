import uuid

import allure

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class NewCampaignPage(BasePage):
    locators = basic_locators.NewCampaignPageLocators()
    url = 'https://target-sandbox.my.com/campaign/new'

    @allure.step("Step 2 special campaign input filling and saving")
    def new_special_campaign(self):
        self.find(self.locators.SPECIAL_CAMPAIGN).click()
        url_input = self.find(self.locators.MAIN_URL_INPUT)
        url_input.clear()
        url_input.send_keys("http://example.com")  # можно параметризовать
        campaign_input = self.find(self.locators.TOP_CAMPAIGN_NAME_INPUT)
        campaign_input.clear()
        campaign_name = str(uuid.uuid1())  # генерим уникальное название новой компании
        campaign_input.send_keys(campaign_name)
        banner_name = self.find(self.locators.BANNER_NAME_INPUT)
        banner_name.clear()
        banner_name.send_keys("Banner")  # можно параметризовать
        banner_button = self.find(self.locators.BANNER_ADD_BUTTON)
        banner_button.click()
        save_campaign_button = self.find(self.locators.SAVE_CAMPAIGN_BUTTON)
        save_campaign_button.click()
        return campaign_name
