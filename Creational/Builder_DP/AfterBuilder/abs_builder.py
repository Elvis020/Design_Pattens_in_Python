from abc import ABC, abstractmethod

from Creational.Builder_DP.AfterBuilder.anothercomputer import AnotherComputer


class AbsBuilder(ABC):

    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = AnotherComputer()

    @abstractmethod
    def build_mainboard(self): raise NotImplementedError

    @abstractmethod
    def get_case(self): raise NotImplementedError

    @abstractmethod
    def install_mainboard(self): raise NotImplementedError

    @abstractmethod
    def install_hard_drive(self): raise NotImplementedError

    @abstractmethod
    def install_video_card(self): raise NotImplementedError