from .AbsAuto import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, name):
        self._name = name

    def start(self):
        print('Unknown car %s' % self._name)

    def stop(self):
        ...
