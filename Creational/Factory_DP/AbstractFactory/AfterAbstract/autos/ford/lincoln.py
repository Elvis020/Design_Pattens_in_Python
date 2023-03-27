
from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.abs_auto import AbsAuto


class LincolnMKS(AbsAuto):
    def start(self):
        print('Lincoln MKS running smoothly.')
    def stop(self):
        print('Lincoln MKS shutting down.')