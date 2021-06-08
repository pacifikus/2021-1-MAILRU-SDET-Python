import random
import string
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from api.socket_client import SocketClient
from mysql.builder import MySQLBuilder
from mysql.client import MysqlClient
from test_settings import APP_HOST, APP_PORT


def pytest_addoption(parser):
    parser.addoption('--url', default=f'http://{APP_HOST}:{APP_PORT}')
    parser.addoption('--selenoid', default=f'http://selenoid_final_project:4444')


@pytest.fixture(scope="session")
def config(request):
    url = request.config.getoption('--url')
    selenoid = request.config.getoption('--selenoid')

    return {"url": url, "selenoid": selenoid}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    selenoid_server = config["selenoid"]
    options = ChromeOptions()
    if selenoid_server:
        capabilities = {'acceptInsecureCerts': True,
                        'browserName': "chrome",
                        'version': '90',
                        "enableVNC": True
                        }

        browser = webdriver.Remote(
            command_executor=f'{selenoid_server}/wd/hub/',
            desired_capabilities=capabilities,
            options=options
        )
    else:
        manager = ChromeDriverManager(version='latest')
        browser = webdriver.Chrome(
            executable_path=manager.install(),
            options=options
        )
    browser.get(url)
    print(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def auth_socket_client():
    client = SocketClient(port=APP_PORT, host=APP_HOST)
    return client


@pytest.fixture(scope='session')
def socket_client():
    client = SocketClient(port=APP_PORT, host=APP_HOST, login_mode=False)
    return client


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root',
                               password='pass', )
    mysql_client.connect()
    mysql_client.create_tables()
    yield mysql_client
    mysql_client.connection.close()


@pytest.fixture(scope='session')
def mysql_builder(mysql_client):
    builder = MySQLBuilder(mysql_client)
    return builder


@pytest.fixture(scope='function')
def userdata():
    base = string.ascii_lowercase
    username = ''.join(random.choice(base) for i in range(7))
    password = ''.join(random.choice(base) for i in range(7))
    email = ''.join(random.choice(base) for i in range(7))
    email += '@gmail.com'
    return {
        'username': username,
        'email': email,
        'password': password,
        'pass_repeat': password,
    }


@pytest.fixture(scope='function')
def random_string():
    base = string.ascii_lowercase
    return ''.join(random.choice(base) for i in range(7))


@pytest.fixture(scope='function')
def added_user(mysql_builder, userdata):
    mysql_builder.add_user(userdata['username'], userdata['password'], userdata['email'])
    return userdata


@pytest.fixture(scope='function')
def blocked_user(mysql_builder, userdata):
    mysql_builder.add_user(userdata['username'], userdata['password'], userdata['email'])
    mysql_builder.block_user(userdata['username'])
    return userdata


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        time.sleep(1)
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
