from .abs_factory import AbsFactory
from Creational.Factory_DP.FullFactory.autos import FordFusion


class FordFactory(AbsFactory):
    def create_auto(self):
        self.ford = ford = FordFusion()
        ford.name = 'Ford Fusion'
        return ford
