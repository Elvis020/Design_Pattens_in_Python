class ChevyVolt:
    def start(self):
        print('Chevrolet Volt is running with shocking power')

    def stop(self):
        print('Chevrolet Volt is shutting down.')


class FordFusion:
    def start(self):
        print('Cool Ford Fusion is running smoothly')

    def stop(self):
        print('Ford Fusion is shutting down.')


class JeepSahara:
    def start(self):
        print('JeepSahara is running ruggedly')

    def stop(self):
        print('JeepSahara is shutting down.')


class NullCar(object):
    def __init__(self, name):
        self._name = name

    def start(self):
        print('Unknown car %s' % self._name)

    def stop(self):
        ...


def getCar(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFusion()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)


for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = getCar(carname)
    car.start()
    car.stop()

# The example above breaks both the Open-Closed Principle and the Dependency Inversion Principle
