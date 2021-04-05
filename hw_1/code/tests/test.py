import pytest
from base import BaseCase
from basic_locators import LOGIN_BUTTON_LOCATOR, LOGOUT_MENU_LOCATOR


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        self.check_page_locator(LOGOUT_MENU_LOCATOR)

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        self.check_page_locator(LOGIN_BUTTON_LOCATOR)
