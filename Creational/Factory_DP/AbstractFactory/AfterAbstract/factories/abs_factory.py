from abc import ABC, abstractmethod


class AbsFactory(ABC):
    @abstractmethod
    def create_economy(self): pass
    
    
    @abstractmethod
    def create_sport(self): pass
    
    @abstractmethod
    def create_luxury(self): pass