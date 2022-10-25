import pytest


class TestLkApi:
    @pytest.fixture(scope='class', autouse=True)
    def setup(self, api_client):
        api_client.post_login()

    def test_api_login(self, api_client):
        assert api_client.session.get('https://target-sandbox.my.com/profile/contacts').url == \
               'https://target-sandbox.my.com/profile/contacts'

