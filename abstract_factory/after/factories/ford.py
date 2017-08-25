from .abs_factory import AbsFactory
from ..autos import ford


class FordFactory(AbsFactory):
    def create_economy(self):
        return ford.FordFiesta()

    def create_sport(self):
        return ford.FordMustang()

    def create_luxury(self):
        return ford.LincolnMKS()
