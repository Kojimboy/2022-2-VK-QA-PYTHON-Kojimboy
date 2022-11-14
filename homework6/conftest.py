import pytest
from sqlalchemy.orm import close_all_sessions

from mysql.client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='1234', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_tables()

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client

    yield client

    close_all_sessions()  # закрываем все сессии
    if not hasattr(request.config, 'workerinput'):
        client.execute_query(f'DROP database {client.db_name}')  # дропаем всю базу после тестов
        # (не дропает в параллельном режиме)
