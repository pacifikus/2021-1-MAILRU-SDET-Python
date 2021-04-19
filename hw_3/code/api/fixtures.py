import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ..api.client import ApiClient


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
    api_client = ApiClient(config['url'])
    api_client.post_login(*credentials)

    cookies_list = []
    for cookie in api_client.session.cookies:
        cookie_dict = {'domain': cookie.domain,
                       'name': cookie.name,
                       'value': cookie.value,
                       'secure': cookie.secure
                       }
        cookies_list.append(cookie_dict)

    return cookies_list


def get_driver(config, download_dir):
    browser_name = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']

    if browser_name == 'chrome':
        options = ChromeOptions()

        if selenoid is not None:
            options.add_experimental_option("prefs",
                                            {"download.default_directory": '/home/selenoid/Downloads'})
            options.add_experimental_option("prefs",
                                            {"profile.default_content_settings.popups": 0})
            options.add_experimental_option("prefs",
                                            {"download.prompt_for_download": False})
            caps = {'browserName': browser_name,
                    'version': '89.0',
                    'sessionTimeout': '2m'}

            if vnc:
                caps['version'] += '_vnc'
                caps['enableVNC'] = True

            browser = webdriver.Remote(selenoid + '/wd/hub',
                                       options=options,
                                       desired_capabilities=caps)

        else:
            options.add_experimental_option("prefs",
                                            {"download.default_directory": download_dir})
            manager = ChromeDriverManager(version='latest', log_level=0)
            browser = webdriver.Chrome(
                executable_path=manager.install(), options=options
            )

    else:
        raise UnsupportedBrowserType(f' Unsupported browser {browser_name}')

    return browser


@pytest.fixture(scope='function')
def driver(config, test_dir):
    url = config['url']
    browser = get_driver(config, download_dir=test_dir)

    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png',
                           attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log',
                          attachment_type=allure.attachment_type.TEXT)
