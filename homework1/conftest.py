import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"browser": browser, "url": url, "headless": headless}


@pytest.fixture(scope='function')
def driver(config, request):
    browser = config["browser"]
    url = config["url"]
    headless = config["headless"]
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
    else:
        chrome_options.add_argument('--start-maximized')
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),
                                  options=chrome_options)

    driver.get(url)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
