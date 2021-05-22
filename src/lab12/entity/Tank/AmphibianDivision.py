from typing import List

from entity.Tank.Amphibian import Amphibian
from entity.Tank.TankDivision import TankDivision


class AmphibianDivision(TankDivision):

    def __init__(self, amphibians: List[Amphibian]):
        super().__init__(amphibians)

    def __str__(self):
        return [str(x) for x in self.tanks]

    def get_troops(self, index):
        iterator = iter(self.tanks)
        while index > 0:
            yield next(iterator)
            index -= 1
