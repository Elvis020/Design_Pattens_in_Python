from Creational.Factory_DP.AbstractFactory.AfterAbstract.autos.abs_auto import AbsAuto


class ChevySpark(AbsAuto):
    def start(self):
        print('Chevy Spark running efficiently.')

    def stop(self):
        print('Chevy Spark shutting down.')
