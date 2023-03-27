from Creational.Builder_DP.BeforeBuilder4.my_computer_builder import MyComputerBuilder

builder = MyComputerBuilder()
builder.build_computer()

computer = builder.get_computer()
computer.display()

