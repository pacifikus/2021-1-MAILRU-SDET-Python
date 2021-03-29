import pytest
from base import BaseCase


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        self.check_page(self.driver.current_url,
                        'https://target.my.com/dashboard')
        self.logout()
        self.driver.save_screenshot('after_login.png')

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        self.check_page(self.driver.current_url, 'https://target.my.com/')
