import pytest
from base import BaseCase
from ..ui.locators import basic_locators


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        ...

    @pytest.mark.UI
    def test_logout(self):
        ...

    @pytest.mark.UI
    def test_change_contact_info(self):
        ...

    @pytest.mark.UI
    def test_main_pages(self):
        ...


