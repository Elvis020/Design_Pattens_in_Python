from Creational.Prototype_DP.ShallowCloning.laptop import Laptop
from Creational.Prototype_DP.ShallowCloning.tower import Tower, MainBoard

laptop1 = Laptop('Laptop 1',
                 'Intel',
                 '32GB',
                 '2TB SSD',
                 'onboard',
                 '1920 x 1080')
# Without tower
# laptop1.display()
# laptop2 = laptop1.clone()
# laptop2.model = 'Laptop 2'
# laptop2.processor = 'AMD '
# print()
# laptop2.display()

# With Tower
tower1 = Tower('Tower 1',
               MainBoard('ASUS', 'Game'),
               'AMD',
               '32GB',
               '2TB SSD',
               'onboard',
               '1920 x 1080')
tower1.display()
tower2 = tower1.clone()
tower2.model = 'Tower 2'
tower2.mainboard.model = 'Business'
print()
tower1.display()
