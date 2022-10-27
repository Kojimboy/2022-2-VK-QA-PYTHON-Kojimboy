import pytest

from base import ApiBase


@pytest.mark.skip('skip')
class TestApiLogin(ApiBase):
    @pytest.fixture(scope='class', autouse=True)
    def setup(self, api_client):
        api_client.post_login()

    def test_api_login(self, api_client):
        assert api_client.session.get('https://target-sandbox.my.com/profile/contacts').url == \
               'https://target-sandbox.my.com/profile/contacts'


@pytest.mark.skip('skip')
@pytest.mark.API
class TestCampaignApi(ApiBase):
    def test_campaign_creation_deletion(self, campaign):
        # print(campaign.campaign_name)
        # print(campaign.banner_name)
        print(f"created id is {campaign.id}")
        assert self.check_active_top_campaign_id(campaign.id) is True


@pytest.mark.API
class TestSegmentApi(ApiBase):
    def test_segment_creation_deletion(self, segment):
        print(segment.segment_name)
        print(f"created id is {segment.id}")
        print(self.check_top_segment_id(segment.id))
