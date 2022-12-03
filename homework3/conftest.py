import os

import pytest

from api.client import ApiClient


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption("--url")
    return {"url": url}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'valid_creds.txt')


@pytest.fixture(scope='session')
def credentials(file_path):  # Берем почту и пароль с файла
    with open(file_path, 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()
    return user, password


@pytest.fixture(scope='session')
def api_client(credentials, config):
    return ApiClient(base_url=config['url'], email=credentials[0], password=credentials[1])


def pytest_make_parametrize_id(config, val):
    return repr(val)
