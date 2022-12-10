import os
import shutil
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage



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
def driver(config, temp_dir, request):  # настройки базового драйвера с условиями
    browser = config['browser']
    url = config['url']
    headless = config["headless"]

    selenoid = config['selenoid']
    vnc = config['vnc']
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    chrome_options.add_argument("force-device-scale-factor=1")  # для масштаба системы 100%
    if request.config.getoption("--headless"):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')

    if selenoid:
        capabilities = {
            'acceptInsecureCerts': True,
            "browserName": "chrome",
            "browserVersion": "108.0",
            "applicationContainers": ["myapp"]
        }
        if vnc:
            capabilities = {
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True,
                    "videoName": "my-cool-video.mp4"
                }
            }
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),
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


def get_driver(browser_name, request):  # Драйвер для куки и логина
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
    if browser_name == 'chrome':
        browser = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),
                                   options=chrome_options)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)
