import pytest

from ..test_api.base import ApiBase


class TestApi(ApiBase):

    @pytest.mark.API
    def test_create_segment(self, api_client):
        name = 'test'
        res = api_client.add_segment(name)
        assert res.status_code == 200
        assert api_client.is_segment_exists(name)
        api_client.remove_segment(name)

    @pytest.mark.API
    def test_remove_segment(self, api_client):
        name = 'test'
        api_client.add_segment(name)
        res = api_client.remove_segment(name)
        assert res.status_code == 204
        assert not api_client.is_segment_exists(name)
