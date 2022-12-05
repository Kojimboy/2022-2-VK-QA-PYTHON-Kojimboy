from sqlalchemy import Column, INTEGER, VARCHAR

from models.base_model import Base


class TopBigReqsModel(Base):
    __tablename__ = 'top_big_reqs'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'url={self.url}, status_code={self.status_code}, size={self.size}, ip={self.ip}'

    url = Column(VARCHAR(200), nullable=False, primary_key=True)
    status_code = Column(INTEGER)
    size = Column(INTEGER)
    ip = Column(VARCHAR(50))
