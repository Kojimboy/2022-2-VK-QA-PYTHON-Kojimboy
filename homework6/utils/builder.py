import re
from collections import Counter

from sqlalchemy import text


def top_methods():
    with open('homework6/files/access.log', 'r') as f:
        log_line = f.readlines()
        method_list = [line.split(' ')[5].strip() for line in log_line]

    uniq_method_sorted = Counter(method_list).most_common()

    uniq_method_sorted = [(i.replace('"', ""), j) for i, j in uniq_method_sorted]  # убираем лишний знак
    uniq_method_sorted.pop()  # убираем последнюю запись

    return uniq_method_sorted


def top_reqs():
    with open('homework6/files/access.log', 'r') as f:
        log_line = f.readlines()
        url_list = [line.split(' ')[6].strip() for line in log_line]

    uniq_url_sorted = Counter(url_list).most_common()

    return uniq_url_sorted[:20]


def top_big_reqs():
    with open('homework6/files/access.log', 'r') as f:
        log_line = f.read()
        client_error_reqs_list = re.findall(r".* 4\d{2} .*", log_line)
        res_list = [line.split(' ')[9::-10] + line.split(' ')[6::-7] + line.split(' ')[8::-9] + line.split(' ')[:1] for
                    line in client_error_reqs_list]
        for el in res_list:
            el[0] = int(el[0])

        res_list.sort(reverse=True)
        return res_list[:20]  # беру 20 записей, потому что ноут улетает при большом количестве записей


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_new_total_methods(self):
        met = top_methods()
        for el in met:
            self.client.execute_query(f"insert into `total_methods` (`method`,`count`) values {el}")

    def create_top_reqs(self):
        top = top_reqs()
        stmt = text(f"""insert ignore into `top_reqs` (`url`,`count`) values (:url, :count)""")
        for el in top:
            stmt = stmt.bindparams(url=el[0], count=el[1])
            self.client.execute_query(stmt)

    def create_top_big_reqs(self):
        top = top_big_reqs()
        stmt = text(f"""insert ignore into `top_big_reqs` (`url`,`status_code`,`size`, `ip`) values (:url, :status_code,
        :size, :ip)""")
        for el in top:
            stmt = stmt.bindparams(size=el[0], url=el[1], status_code=el[2], ip=el[3])
            self.client.execute_query(stmt)
