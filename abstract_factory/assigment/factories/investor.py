from .abs_factory import AbsFactory
from ..customers import investors


class InvestorFactory(AbsFactory):
    def create_government(self):
        return investors.Government

    def create_retail(self):
        return investors.Retail

    def create_commercial(self):
        return investors.Commercial
