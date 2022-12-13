import os
import shutil
import sys
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from faker import Faker

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.reg_page import RegPage

fake = Faker()


@pytest.fixture()
def driver(config, temp_dir, request):  # настройки базового драйвера с условиями(перед началом всех тестов)
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


@pytest.fixture(scope='session')
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'valid_creds.txt')


@pytest.fixture(scope='session')
def credentials(file_path):  # Берем имя и пароль с файла
    # import pdb;
    # pdb.set_trace()
    with open(file_path, 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()
    return user, password


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
    var = request._pyfuncitem.nodeid
    var = var.replace("/", "_").replace(":", "_").replace(" ", "_")  # исправляем путь для windows
    test_dir = os.path.join(request.config.base_temp_dir, var)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def random_fields():
    # fields = []
    # # if not hasattr(config, 'workerinput'):
    # fields.append(fake.first_name())
    # fields.append(fake.last_name())
    # fields.append(fake.user_name()[:])  # надо сделать так чтобы длину можно было задать
    # fields.append(fake.email())
    # fields.append(fake.password(special_chars=False))
    fields = []
    fields.append("Johny")
    fields.append("Johnson")
    fields.append("JohnyName")
    fields.append("example@mail.net")
    fields.append("fake_password")
    return fields


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
    driver.get(BasePage.url)
    return BasePage(driver=driver)


@pytest.fixture
def reg_page(driver):
    driver.get(RegPage.url)
    return RegPage(driver=driver)


@pytest.fixture
def login_page(driver):
    driver.get(LoginPage.url)
    return LoginPage(driver=driver)
