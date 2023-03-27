from .abs_factory import AbsFactory
from Creational.Factory_DP.FullFactory.autos import JeepSahara


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.jeep = jeep = JeepSahara()
        jeep.name = 'Jeep Sahara'
        return jeep
