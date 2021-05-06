import pytest

from mysql.builder import MySQLBuilder
from mysql.models import TotalCount, CountByType, TopMostFrequent, \
    TopBiggestClientError, TopFrequentServerError


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client

    @pytest.fixture(scope='session', autouse=True)
    def setup_data(self, mysql_client):
        self.mysql_builder = MySQLBuilder(mysql_client, path='../access.log')
        self.prepare()


class TestMysql(MySQLBase):

    def prepare(self):
        self.mysql_builder.run_all()

    def get_rows(self, query_type):
        rows = self.mysql.session.query(query_type).all()
        print(rows)
        return rows

    def get_query(self, query_type):
        rows = self.mysql.session.query(query_type)
        print(rows)
        return rows

    def test_count_total(self):
        result = self.get_rows(TotalCount)

        assert len(result) == 1
        assert result[0].count == 225133

    def test_count_by_type(self):
        result = self.get_query(CountByType)

        assert len(result.all()) == 4
        assert result.filter_by(type_name='POST').first().count == 102503
        assert result.filter_by(type_name='GET').first().count == 122095
        assert result.filter_by(type_name='HEAD').first().count == 528
        assert result.filter_by(type_name='PUT').first().count == 6

    def test_top_10(self):
        result = self.get_query(TopMostFrequent)

        assert len(result.all()) == 10
        assert result.filter_by(url='/administrator/index.php')\
                     .first().count == 103932

    def test_top_5_4xx_requests(self):
        result = self.get_rows(TopBiggestClientError)

        assert len(result) == 5

    def top_5_5xx_users(self):
        result = self.get_rows(TopFrequentServerError)

        assert len(result) == 5
        assert result.filter_by(url='189.217.45.73') \
                     .first().count == 225
