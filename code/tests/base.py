import pytest
import basic_locators
from creds import LOGIN, PASS
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseCase:
    driver = None
    config = None

    def find(self, locator):
        delay = 5
        elem = WebDriverWait(self.driver, delay).until(
            EC.presence_of_element_located(locator)
        )
        return elem

    def click(self, elem):
        try:
            self.find(elem).click()
        except TimeoutException:
            print(1)
            self.find(elem).click()

    def send_keys(self, elem, key):
        try:
            self.find(elem).send_keys(key)
        except TimeoutException:
            self.find(elem).send_keys(key)

    def login(self):
        self.click(basic_locators.LOGIN_BUTTON_LOCATOR)
        self.send_keys(basic_locators.LOGIN_INPUT_LOCATOR, LOGIN)
        self.send_keys(basic_locators.PASS_INPUT_LOCATOR, PASS)
        self.click(basic_locators.LOGIN_SUBMIT_LOCATOR)

    def logout(self):
        time.sleep(5)
        self.click(basic_locators.LOGOUT_MENU_LOCATOR)
        time.sleep(5)
        self.find(basic_locators.LOGOUT_LINK_LOCATOR).click()

    def check_page_locator(self, target_locator):
        assert self.find(target_locator)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
