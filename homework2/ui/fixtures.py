import os
import shutil
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.main_page import MainPage
from ui.pages.new_campaign_page import NewCampaignPage


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture()
def driver(config, temp_dir, request):  # настройки драйвера с условиями
    browser = config['browser']
    url = config['url']
    headless = config["headless"]
    # selenoid = config['selenoid']
    # vnc = config['vnc']
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    if request.config.getoption("--headless"):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
    # if selenoid:
    #     capabilities = {
    #         'browserName': 'chrome',
    #         'version': '106.0',
    #     }
    #     if vnc:
    #         capabilities['enableVNC'] = True
    #     driver = webdriver.Remote(
    #         'http://127.0.0.1:4444/wd/hub',
    #         options=options,
    #         desired_capabilities=capabilities
    #     )
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager("105.0.5195.19").install(),
                                  options=chrome_options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def get_driver(browser_name):  # Драйвер для куки
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager("105.0.5195.19").install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)


@pytest.fixture
def new_campaign_page(driver):
    return NewCampaignPage(driver=driver)
