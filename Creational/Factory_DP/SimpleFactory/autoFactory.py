from inspect import getmembers, isclass, isabstract

import autos


class AutoFactory(object):
    autos = {}  # Key= car model, Value =class of car

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        # Looks for concrete classes
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))

        # For every concrete class found, it checks if it is a subclass of AbsAuto and then adds to the autos dictionary
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update({name:_type})

    def create_instances(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        return autos.NullCar(carname)
