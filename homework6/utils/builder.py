from collections import Counter

from sqlalchemy import text

from models import total_methods
from models.total_methods import TotalMethodsModel


def top_methods():
    with open('homework6/files/access.log', 'r') as f:
        log_line = f.readlines()
        method_list = [line.split(' ')[5].strip() for line in log_line]

    uniq_method_sorted = Counter(method_list).most_common()

    uniq_method_sorted = [(i.replace('"', ""), j) for i, j in uniq_method_sorted]  # убираем лишний знак
    uniq_method_sorted.pop()  # убираем последнюю запись

    top_methods_string = ", ".join(map(str, uniq_method_sorted))  # строка для insert запроса
    return uniq_method_sorted


def top_reqs():
    with open('homework6/files/access.log', 'r') as f:
        log_line = f.readlines()
        url_list = [line.split(' ')[6].strip() for line in log_line]

    uniq_url_sorted = Counter(url_list).most_common()

    # top_reqs_string = ", ".join(map(str, uniq_url_sorted))  # строка для insert запроса
    return uniq_url_sorted[0:10]


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_new_total_methods(self):
        met = top_methods()
        # import pdb;
        # pdb.set_trace()
        for el in met:
            self.client.execute_query(f"insert into `total_methods` (`method`,`count`) values {el}")

    def create_top_reqs(self):
        topich = top_reqs()
        # import pdb;
        # pdb.set_trace()
        stmt = text(f"""insert ignore into `top_reqs` (`url`,`count`) values (:url, :count)""")
        for el in topich:
            stmt = stmt.bindparams(url=el[0], count=el[1])
            self.client.execute_query(stmt)

