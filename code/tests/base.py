import pytest
import basic_locators
from creds import LOGIN, PASS
import time


class BaseCase:
    driver = None
    config = None

    def find(self, locator):
        return self.driver.find_element(*locator)

    def login(self):
        self.find(basic_locators.LOGIN_BUTTON_LOCATOR).click()
        self.find(basic_locators.LOGIN_INPUT_LOCATOR).send_keys(LOGIN)
        self.find(basic_locators.PASS_INPUT_LOCATOR).send_keys(PASS)
        self.find(basic_locators.LOGIN_SUBMIT_LOCATOR).click()

    def logout(self):
        time.sleep(5)
        self.find(basic_locators.LOGOUT_MENU_LOCATOR).click()
        time.sleep(5)
        self.find(basic_locators.LOGOUT_LINK_LOCATOR).click()

    def check_page_locator(self, target_locator):
        time.sleep(5)
        assert self.driver.find_elements(*target_locator)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
