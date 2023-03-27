from Creational.Builder_DP.AfterBuilder.budget_box_builder import MyBudgetBoxBuilder
from Creational.Builder_DP.AfterBuilder.director import Director
from Creational.Builder_DP.AfterBuilder.mycomputer_builder import MyComputerBuilder

computer_builder = Director(MyComputerBuilder)
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

print('*'*10)
budget_computer_builder = Director(MyBudgetBoxBuilder)
budget_computer_builder.build_computer()
budget_computer = budget_computer_builder.get_computer()
budget_computer.display()



