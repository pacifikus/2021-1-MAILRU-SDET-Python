import allure
import pytest

from .base import BaseCase
from .creds import LOGIN, PASS


class TestAuthorization(BaseCase):
    is_authorized = False

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Invalid login with valid password')
    @pytest.mark.UI
    def test_invalid_login(self):
        invalid_login = '123123'

        self.base_page.login(invalid_login, PASS)
        assert not self.base_page.is_authorized()

    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Valid login with invalid password')
    @pytest.mark.UI
    def test_invalid_pass(self):
        invalid_pass = '123123'
        self.base_page.login(LOGIN, invalid_pass)
        assert not self.base_page.is_authorized()


class TestSegments(BaseCase):

    @allure.epic('UI tests')
    @allure.feature('Segments')
    @allure.story('Add new segment to segments list')
    @pytest.mark.UI
    def test_add_segment(self):

        segments_page = self.dashboard_page.go_to_segments()
        segments_page.add_segment()
        assert segments_page.has_segments()

        segments_page.remove_segment()

    @allure.epic('UI tests')
    @allure.feature('Segments')
    @allure.story('Remove the added segment from the segments list')
    @pytest.mark.UI
    def test_remove_segment(self):
        segments_page = self.dashboard_page.go_to_segments()
        segments_page.add_segment()
        segments_page.remove_segment()
        assert not segments_page.has_segments()


class TestCampaigns(BaseCase):

    @allure.epic('UI tests')
    @allure.feature('Campaigns')
    @allure.story('Add new campaign to campaigns list')
    @pytest.mark.UI
    def test_add_campaign(self):
        campaign_name = 'test'
        self.logger.info('Add new campaign')
        self.dashboard_page.add_campaign(campaign_name)
        assert self.dashboard_page.is_campaign_exists(campaign_name)

        self.dashboard_page.remove_campaign()
