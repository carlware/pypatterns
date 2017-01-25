from ..abs_cus import AbsCust


class Commercial(AbsCust):
    def report_type(self):
        print('"%s" is a commercial investor.' % self.name)
