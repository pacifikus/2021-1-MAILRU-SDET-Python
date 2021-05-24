from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalCount(Base):
    __tablename__ = 'total_count'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Total Count(" \
               f"id='{self.id}'," \
               f"count='{self.count})>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)


class CountByType(Base):
    __tablename__ = 'count_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Count by type(" \
               f"id='{self.id}'," \
               f"count='{self.count}', " \
               f"type_name='{self.type_name})>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    type_name = Column(String(6), nullable=False)


class TopMostFrequent(Base):
    __tablename__ = 'top_most_frequent_urls'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Total Count(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"count='{self.count})>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(250), nullable=False)
    count = Column(Integer, nullable=False)


class TopBiggestClientError(Base):
    __tablename__ = 'top_biggest_400_urls'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Total Count(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"code='{self.code}'," \
               f"size='{self.size}'," \
               f"ip='{self.ip})>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(250), nullable=False)
    code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(16), nullable=False)


class TopFrequentServerError(Base):
    __tablename__ = 'top_most_frequent_500'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Total Count(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}'," \
               f"count='{self.count})>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16), nullable=False)
    count = Column(Integer, nullable=False)
