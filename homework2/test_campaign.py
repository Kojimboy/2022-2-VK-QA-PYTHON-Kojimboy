import allure
import pytest

from base import BaseCase
from ui.pages.campaign_page import CampaignPage
from ui.pages.new_campaign_page import NewCampaignPage


@pytest.mark.UI
class TestCampaign(BaseCase):
    @allure.step("Step 1 start new special campaign test ")
    def test_new_special_campaign(self):
        self.logger.info('Go to new campaign page')
        self.driver.get(NewCampaignPage.url)
        new_campaign_page = NewCampaignPage(self.driver)
        self.logger.info('Choose and create special campaign')
        new_campaign_name = new_campaign_page.new_special_campaign()
        self.logger.info('Check created campaign name')
        campaign_page = CampaignPage(self.driver)
        assert new_campaign_name == campaign_page.get_created_campaign_name()
