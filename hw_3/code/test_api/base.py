import pytest


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, credentials):
        self.api_client = api_client
        if self.authorize:
            print(*credentials)
            self.api_client.post_login(*credentials)
