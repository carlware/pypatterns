from .abs_factory import AbsFactory
from ..autos import gm


class GMFactory(AbsFactory):
    def create_economy(self):
        return gm.ChevySpark()

    def create_sport(self):
        return gm.CadillacCTS()

    def create_luxury(self):
        return gm.ChevyCamaro()
