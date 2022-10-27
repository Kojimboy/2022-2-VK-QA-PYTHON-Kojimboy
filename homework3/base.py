import time

import pytest

from api.builder import Builder


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder()

        if self.authorize:
            self.api_client.post_login()

    def create_campaign(self, campaign_name, banner_name):
        req = self.api_client.post_campaign_create(campaign_name=campaign_name, banner_name=banner_name)
        assert "id" in req
        #
        # print(req)
        return req['id']

    def check_active_top_campaign_id(self, campaign_id):  # проверяет активные компании на id
        found = False
        all_campaigns_fields_dict = self.api_client.get_top_active_campaign_id()
        for item in all_campaigns_fields_dict["items"]:
            print(f"top campaign id in list is {item['id']}")
            if item['id'] == campaign_id:
                found = True
                break
        return found

    def delete_campaign(self, campaign_id):
        req = self.api_client.post_campaign_delete(campaign_id)
        # тут засунуть проверку еще одного запроса
        assert req.status_code == 204
        return req

    @pytest.fixture(scope='function')
    def campaign(self):
        campaign_data = self.builder.segment()
        campaign_id = self.create_campaign(campaign_name=campaign_data.segment_name,
                                           banner_name=campaign_data.banner_name)
        campaign_data.id = campaign_id
        # до теста
        yield campaign_data
        # после теста
        self.delete_campaign(campaign_id=campaign_id)
        assert self.check_active_top_campaign_id(campaign_id=campaign_id) is False

    @pytest.fixture(scope='function')
    def segment(self):
        segment_data = self.builder.segment()
        segment_id = self.create_segment(segment_name=segment_data.segment_name)
        segment_data.id = segment_id
        # до теста
        yield segment_data
        # после теста
        time.sleep(15)
        self.api_client.post_segment_delete(segment_id)
        assert self.check_top_segment_id(segment_id=segment_id) is False

    def check_top_segment_id(self, segment_id):  # проверяет id сегмента
        found = False
        all_segment_fields_dict = self.api_client.get_top_segment_id()
        for item in all_segment_fields_dict["items"]:
            print(f"top segment id in list is {item['id']}")
            if item['id'] == segment_id:
                found = True
                break
        return found

    def create_segment(self, segment_name):
        req = self.api_client.post_segment_create(segment_name=segment_name)
        assert "id" in req

        print(req)
        return req['id']

