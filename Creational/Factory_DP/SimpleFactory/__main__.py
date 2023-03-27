from autoFactory import AutoFactory

factory = AutoFactory()

for carname in 'ChevyVolt', 'FordFusion', 'JeepSahara', 'Tesla Roadster':
    car = factory.create_instances(carname)
    car.start()
    car.stop()
