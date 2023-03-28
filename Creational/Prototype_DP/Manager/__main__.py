# With Laptop
from Creational.Prototype_DP.Manager.laptop import Laptop
from Creational.Prototype_DP.Manager.prototype_manager import PrototypeManager
from Creational.Prototype_DP.Manager.tower import Tower, MainBoard

manager = PrototypeManager()
laptop1 = Laptop('Laptop 1',
                 'Intel',
                 '32GB',
                 '2TB SSD',
                 'onboard',
                 '1920 x 1080')
laptop1.display()
manager |= {'Laptop 1': laptop1}
laptop2 = manager['Laptop 1'].clone()
print()
laptop2.model = 'Laptop 2'
laptop2.processor = 'AMD'
laptop2.display()
print()

# With Tower
tower1 = Tower('Tower 1',
               MainBoard('ASUS', 'Game'),
               'AMD',
               '32GB',
               '2TB SSD',
               'onboard',
               '1920 x 1080')
tower1.display()
manager |= {'Tower 1': tower1}
tower2 = manager['Tower 1'].clone()
tower2.model = 'Tower 2'
tower2.mainboard.model = 'Business'
print()
tower2.display()
print()
tower1.display()
