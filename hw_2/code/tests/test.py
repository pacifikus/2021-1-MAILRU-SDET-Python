import allure
import pytest

from .base import BaseCase
from .creds import LOGIN, PASS


class TestAuthorization(BaseCase):

    is_authorized = False

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.story('Invalid login with valid password')
    @pytest.mark.UI
    def test_invalid_login(self):
        invalid_login = '123123'

        with allure.step('Trying to log in'):
            self.base_page.login(invalid_login, PASS)
        assert not self.base_page.is_authorized()

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.story('Valid login with invalid password')
    @pytest.mark.UI
    def test_invalid_pass(self):
        invalid_pass = '123123'

        with allure.step('Trying to log in'):
            self.base_page.login(LOGIN, invalid_pass)
        assert not self.base_page.is_authorized()


class TestSegments(BaseCase):

    @allure.epic('UI tests')
    @allure.feature('Segments')
    @allure.story('Add new segment to segments list')
    @pytest.mark.UI
    def test_add_segment(self):
        with allure.step('Go to segments list'):
            segments_page = self.dashboard_page.go_to_segments()

        with allure.step('Add new segment to segments list'):
            segments_page.add_segment()

        assert segments_page.has_segments()

        with allure.step('Remove the added segment'):
            segments_page.remove_segment()

    @allure.epic('UI tests')
    @allure.feature('Segments')
    @allure.story('Remove the added segment from the segments list')
    @pytest.mark.UI
    def test_remove_segment(self):
        with allure.step('Go to segments list'):
            segments_page = self.dashboard_page.go_to_segments()

        with allure.step('Add new segment to segments list'):
            segments_page.add_segment()

        with allure.step('Remove the added segment'):
            segments_page.remove_segment()

        assert not segments_page.has_segments()


class TestCampaigns(BaseCase):

    @allure.epic('UI tests')
    @allure.feature('Campaigns')
    @allure.story('Add new campaign to campaigns list')
    @pytest.mark.UI
    def test_add_campaign(self):
        self.logger.info('Add new campaign')

        with allure.step('Add new campaign'):
            self.dashboard_page.add_campaign()
            assert self.dashboard_page.has_campaigns()

        with allure.step('Remove the added campaign'):
            self.dashboard_page.remove_campaign()
