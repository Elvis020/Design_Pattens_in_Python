from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.gm.spark import ChevySpark
from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.gm.camaro import ChevyCamaro
from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.gm.cadillac import CadillacCTS
from Creational.Factory_DP.AbstractFactory.AfterAbstract.factories.abs_factory import AbsFactory



class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
