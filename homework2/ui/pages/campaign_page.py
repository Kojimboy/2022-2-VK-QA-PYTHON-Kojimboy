import allure

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class CampaignPage(BasePage):
    locators = basic_locators.CampaignPageLocators()
    url = 'https://target-sandbox.my.com/dashboard#'

    @allure.step("Get created campaign name for assertion")
    def get_created_campaign_name(self):
        self.driver.get(CampaignPage.url)
        cell = self.find(self.locators.TOP_CAMPAIGN_CELL)
        return cell.get_attribute("title")
