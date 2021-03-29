import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', default='http://target.my.com')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope='session')
def driver(config):
    url = config['url']
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome('')
    browser.get(url)
    browser.set_window_size(1400, 1000)
    yield browser
    browser.close()
