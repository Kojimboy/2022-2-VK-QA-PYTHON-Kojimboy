from models.base_model import Base
from sqlalchemy import Column, INTEGER, VARCHAR


class TopReqsModel(Base):

    __tablename__ = 'top_reqs'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'url={self.url}, count={self.count}'

    url = Column(VARCHAR(200), nullable=False, primary_key=True)
    count = Column(INTEGER)
