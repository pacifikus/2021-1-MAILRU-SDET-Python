import pytest

from ..test_api.base import ApiBase


class TestApi(ApiBase):

    @pytest.mark.API
    def test_create_segment(self, api_client):
        res, segment_id = api_client.add_segment()
        assert res.status_code == 200
        assert segment_id in api_client.segments_ids
        api_client.remove_segment(segment_id)

    @pytest.mark.API
    def test_remove_segment(self, api_client):
        res, segment_id = api_client.add_segment()
        res = api_client.remove_segment(segment_id)
        assert res.status_code == 204
        assert segment_id not in api_client.segments_ids
