import pytest

from models.top_big_reqs import TopBigReqsModel
from models.top_reqs import TopReqsModel
from models.total_methods import TotalMethodsModel
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.client)

    def get_methods(self, **filters):
        self.client.session.commit()
        return self.client.session.query(TotalMethodsModel). \
            filter_by(**filters).order_by(TotalMethodsModel.count.desc()).all()

    def get_reqs(self, top, **filters):
        self.client.session.commit()
        return self.client.session.query(TopReqsModel). \
            filter_by(**filters).order_by(TopReqsModel.count.desc()).limit(top).all()

    def get_big_reqs(self, top, **filters):
        self.client.session.commit()
        return self.client.session.query(TopBigReqsModel). \
            filter_by(**filters).order_by(TopBigReqsModel.size.desc()).limit(top).all()
