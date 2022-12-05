from base import BaseCase


class TestMysql(BaseCase):

    def test_top_methods(self):
        self.builder.create_new_total_methods()
        methods = self.get_methods()
        assert len(methods) == 4

    def test_top_reqs(self):
        self.builder.create_top_reqs()
        reqs = self.get_reqs(top=10)
        assert len(reqs) == 10

    def test_top_big_reqs(self):
        self.builder.create_top_big_reqs()
        big_reqs = self.get_big_reqs(top=5)
        assert len(big_reqs) == 5
