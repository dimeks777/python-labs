from abc import ABC, abstractmethod


class Unit(ABC):

    @abstractmethod
    def calculate_battle_efficiency(self):
        pass

    @abstractmethod
    def damage(self):
        pass

    @staticmethod
    def general_info():
        print('This object is an instance of battle unit')
