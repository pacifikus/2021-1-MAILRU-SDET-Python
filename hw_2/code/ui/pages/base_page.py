import logging

import allure
from selenium.common.exceptions import StaleElementReferenceException, \
    TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators.basic_locators import LoginPageLocators

CLICK_RETRY = 3
BASE_TIMEOUT = 10

logger = logging.getLogger('test')


class BasePage(object):
    locators = LoginPageLocators()

    def __init__(self, driver):
        self.driver = driver
        logger.info(f'{self.__class__.__name__} page is opening...')

    def find(self, locator, timeout=None, has_to_be_clickable=False):
        if has_to_be_clickable:
            return self.wait(timeout).until(
                EC.element_to_be_clickable(locator)
            )
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def search(self, query):
        search = self.find(self.locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        self.click(self.locators.GO_LOCATOR)

    @allure.step('Clicking {locator}')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {locator}.'
                        f' Try {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def send_keys(self, locator, key, timeout=None, has_to_be_clickable=False):
        element = self.find(locator, timeout=timeout,
                            has_to_be_clickable=has_to_be_clickable)
        element.send_keys(key)

    @allure.step("Trying to log in")
    def login(self, login_value, pass_value):
        self.click(self.locators.LOGIN_BUTTON_LOCATOR)
        self.send_keys(self.locators.LOGIN_INPUT_LOCATOR, login_value)
        self.send_keys(self.locators.PASS_INPUT_LOCATOR, pass_value)
        self.click(self.locators.LOGIN_SUBMIT_LOCATOR)
        return self.driver

    def is_authorized(self):
        try:
            self.find(self.locators.LOGIN_BUTTON_LOCATOR)
            return True
        except TimeoutException:
            return False
