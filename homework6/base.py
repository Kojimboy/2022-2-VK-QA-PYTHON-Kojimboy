import pytest

from models.top_reqs import TopReqsModel
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder
from models.total_methods import TotalMethodsModel


class BaseCase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.client)
        self.prepare()

    def get_methods(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TotalMethodsModel).\
            filter_by(**filters).order_by(TotalMethodsModel.count.desc()).all()

    def get_reqs(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TopReqsModel).\
            filter_by(**filters).all()
