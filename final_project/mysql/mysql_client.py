import sqlalchemy
from sqlalchemy.orm import sessionmaker


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
        # url = f"mysql+pymysql://{self.host}:{self.port}/{self.db_name}"
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def drop_users(self):
        self.execute_query("delete from test_users where id!= 1;")

    def drop_logged_test_user(self):
        self.execute_query("update test_users set active = NULL, start_active_time = NULL where id = 1;")
