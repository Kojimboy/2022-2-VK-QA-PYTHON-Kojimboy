import os
import shutil
import sys

import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target-sandbox.my.com/')
    parser.addoption('--headless', action='store_true')
    # parser.addoption('--debug_log', action='store_true')
    # parser.addoption('--selenoid', action='store_true')
    # parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def base_temp_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    headless = request.config.getoption("--headless")
    return {"browser": browser, "url": url, "headless": headless}


