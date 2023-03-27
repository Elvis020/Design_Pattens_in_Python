from .AbsAuto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print('Chevrolet Volt is running with shocking power')

    def stop(self):
        print('Chevrolet Volt is shutting down.')