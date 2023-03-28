import copy

from Creational.Prototype_DP.ShallowCloning.abs_computer import AbsComputer
from Creational.Prototype_DP.ShallowCloning.abs_prototype import AbsPrototype


class MainBoard:
    manufacturer: str
    model: str

    def __init__(self, manufacture, model):
        self.manufacturer = manufacture
        self.model = model


class Tower(AbsComputer, AbsPrototype):
    def __init__(self, model, mainboard, processor, memory, hard_drive, graphics, monitor):
        self.model = model
        self.mainboard = mainboard
        self.processor = processor
        self.memory = memory
        self.hard_drive = hard_drive
        self.graphics = graphics
        self.monitor = monitor

    def display(self):
        print("Custom Computer: " + self.model)
        print(f"\t{'Mainboard':>10}: {self.mainboard.model}")
        print(f"\t{'Processor':>10}: {self.processor}")
        print(f"\t{'Memory':>10}: {self.memory}")
        print(f"\t{'Hard drive':>10}: {self.hard_drive}")
        print(f"\t{'Graphics':>10}: {self.graphics}")
        print(f"\t{'Screen':>10}: {self.monitor if self.monitor else 'None'}")

    def clone(self):
        return copy.deepcopy(self)
