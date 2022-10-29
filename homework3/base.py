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

    @pytest.fixture(scope='function')
    def campaign(self):
        campaign_data = self.builder.campaign()
        campaign_id = self.create_campaign(campaign_name=campaign_data.campaign_name,
                                           banner_name=campaign_data.banner_name)
        campaign_data.id = campaign_id
        # до теста
        yield campaign_data
        # после теста
        self.delete_campaign(campaign_id=campaign_id)
        assert self.check_active_top_campaign_id(campaign_id=campaign_id) is False

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
    def segment(self, object_type, source):
        segment_data = self.builder.segment(object_type=object_type)
        # if source_id is None # передать source id в post_segment_create

        segment_id = self.create_segment(segment_name=segment_data.segment_name,
                                         object_type=segment_data.object_type,
                                         source_id=source.object_id)
        segment_data.id = segment_id
        # до теста
        yield segment_data
        # после теста
        # time.sleep(20)
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

    def create_segment(self, segment_name, object_type, source_id):
        req = self.api_client.post_segment_create(segment_name=segment_name, object_type=object_type,
                                                  source_id=source_id)
        assert "id" in req
        return req['id']

    @pytest.fixture(scope='function')
    def source(self, url):
        source_data = self.builder.source_group(url=url)
        source_id = self.get_source_id(source_data.url) if url else None
        source_data.object_id = source_id

        if url:
            vk_source_fields_dict = self.api_client.post_vk_source_create(source_data.object_id)  # создаем группу
            for item in vk_source_fields_dict["items"]:
                source_data.vk_id = item['id']
        # до теста
        yield source_data
        # после теста
        if url:
            self.api_client.post_vk_source_delete(source_data.vk_id)
            assert self.check_source(source_data.vk_id) is False

    def get_source_id(self, url):
        all_source_fields_dict = self.api_client.get_vk_source_id_in_search(url)
        for item in all_source_fields_dict["items"]:
            vk_id = item['id']
        return vk_id

    def check_source(self, vk_id):  # проверяет id группы
        found = False
        all_sources_in_list_fields_dict = self.api_client.get_vk_source_id_in_list()
        for item in all_sources_in_list_fields_dict["items"]:
            if item['id'] == vk_id:
                found = True
                break
        return found
