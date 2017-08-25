from .abs_factory import AbsFactory
from ..customers import savers


class SaversFactory(AbsFactory):
    def create_government(self):
        return savers.Government

    def create_retail(self):
        return savers.Retail

    def create_commercial(self):
        return savers.Commercial
