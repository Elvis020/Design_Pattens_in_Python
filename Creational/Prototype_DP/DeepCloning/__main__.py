from Creational.Prototype_DP.DeepCloning.tower import Tower, MainBoard

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
tower2.display()
print()
tower1.display()
