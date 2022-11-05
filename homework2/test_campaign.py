import allure
import pytest

from base import BaseCase
from ui.pages.campaign_page import CampaignPage
from ui.pages.new_campaign_page import NewCampaignPage


@pytest.mark.UI
class TestCampaign(BaseCase):
    @allure.step("Go to new campaign page ")
    def test_special_campaign(self):
        self.driver.get(NewCampaignPage.url)
        new_campaign_page = NewCampaignPage(self.driver)
        new_campaign_name = new_campaign_page.new_special_campaign()
        self.logger.info('Check created campaign name')
        campaign_page = CampaignPage(self.driver)
        assert new_campaign_name == campaign_page.get_created_campaign_name()
