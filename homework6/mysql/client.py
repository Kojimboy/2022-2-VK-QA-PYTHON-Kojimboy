import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.base_model import Base

# эти импорты нужны для создания таблиц

from models.total_methods import TotalMethodsModel
from models.top_reqs import TopReqsModel
from models.top_big_reqs import TopBigReqsModel


class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = '3306'
        self.password = password
        self.host = '127.0.0.1'
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')

    def create_tables(self):
        Base.metadata.create_all(self.engine)  # создаем все нужные таблицы

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def drop_db(self):
        self.execute_query(f'DROP database {self.db_name}')
