from Creational.Builder_DP.BeforeBuilder3.computer import MyComputer


class Computer:
    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = MyComputer()
        computer.case = 'Coolermaster'
        computer.mainboard = 'MSI'
        computer.cpu = 'Intel Core-i9'
        computer.memory = '2 X 16GB'
        computer.hard_drive = 'SSD 2TB'
        computer.video_card = 'GeForce'
