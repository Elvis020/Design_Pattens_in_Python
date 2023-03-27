from Creational.Builder_DP.BeforeBuilder3.my_computer import Computer

builder = Computer()
builder.build_computer()

computer = builder.get_computer()
computer.display()

