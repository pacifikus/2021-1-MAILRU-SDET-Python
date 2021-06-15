import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from mysql.models import Base
from test_settings import MYSQL_HOST, MYSQL_PORT, MYSQL_DB


class MysqlClient:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.db_name = MYSQL_DB

        self.host = MYSQL_HOST
        self.port = MYSQL_PORT

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self):

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:'
            f'{self.password}@{self.host}:'
            f'{self.port}/{self.db_name}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=False,
                                    expire_on_commit=False
                                    )()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_tables(self, table_names=('test_users',)):
        for table_name in table_names:
            if not inspect(self.engine).has_table(table_name):
                print(table_name)
                Base.metadata.tables[table_name].create(self.engine)
