from base import BaseCase


class TestMysql(BaseCase):

    def prepare(self):
        self.builder.create_new_total_methods()

    def test_top_methods(self):
        methods = self.get_methods()
        assert len(methods) == 4

    # def test_top_reqs(self):
    #     reqs = self.get_reqs()
    #     print(reqs)
    #     # import pdb;
    #     # pdb.set_trace()
    #     # assert len(reqs) == 4


class TestSecond(BaseCase):

    def prepare(self):
        self.builder.create_top_reqs()

    def test_top_reqs(self):
        reqs = self.get_reqs()
        print(reqs)

        pass
        # assert len(reqs) == 4
