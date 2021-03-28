import pytest
from ..ui.locators import basic_locators
from ..utils.creds import LOGIN, PASS


class BaseCase:
    driver = None
    config = None

    def find(self, locator):
        return self.driver.find_element(*locator)

    def login(self):
        self.find().send_keys(LOGIN)
        self.find().send_keys(PASS)
        self.find().click()


    def check_page(self, page, target_locator):
        ...

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

