from models.base_model import Base
from sqlalchemy import Column, INTEGER, VARCHAR


class TotalMethodsModel(Base):

    __tablename__ = 'total_methods'
    __table_arg__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f'count={self.count}, method_name={self.method}'

    method = Column(VARCHAR(50), nullable=False, primary_key=True, unique=True)
    count = Column(INTEGER)
