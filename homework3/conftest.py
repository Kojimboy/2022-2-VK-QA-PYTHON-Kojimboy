import pytest

from api.client import ApiClient


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"browser": browser, "url": url, "headless": headless}


@pytest.fixture(scope='session')
def credentials():  # Берем почту и пароль с файла
    with open('homework3/files/valid_creds.txt', 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()
    return user, password


@pytest.fixture(scope='session')
def api_client(credentials, config):
    return ApiClient(base_url=config['url'], email=credentials[0], password=credentials[1])


def pytest_make_parametrize_id(config, val):
    return repr(val)
