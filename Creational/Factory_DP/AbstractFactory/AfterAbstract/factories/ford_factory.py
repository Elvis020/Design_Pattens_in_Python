from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.ford.fiesta import FordFiesta
from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.ford.mustang import FordMustang
from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.ford.lincoln import LincolnMKS
from Creational.Factory_DP.AbstractFactory.AfterAbstract.factories.abs_factory import AbsFactory


class FordFactory(AbsFactory):

    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()