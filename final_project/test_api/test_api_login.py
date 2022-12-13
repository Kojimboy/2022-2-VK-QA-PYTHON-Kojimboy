import pytest

from api.api_client import ResponseStatusCodeException
from base import ApiBase
from configuration.myapp_config import APP_SERVICE, APP_PORT


@pytest.mark.API
class TestApiLogin(ApiBase):
    @pytest.mark.Smoke
    def test_api_login(self, api_client):
        self.logger.info('Check success login with API')
        assert api_client.session.get(f"http://{APP_SERVICE}:{APP_PORT}/").url == \
               f"http://{APP_SERVICE}:{APP_PORT}/welcome/"
