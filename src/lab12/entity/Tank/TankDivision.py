from typing import List

from entity.Tank.Tank import Tank


class TankDivision:

    def __init__(self, tanks: List[Tank]):
        self.tanks = tanks

    def __iter__(self):
        return TankIterator(self)


class TankIterator:

    def __init__(self, tank_division: TankDivision):
        self.tank_division = tank_division
        self._index = 0

    def __next__(self):
        if self._index < (len(self.tank_division.tanks)):
            result = (self.tank_division.tanks[self._index])
            self._index += 1
            return result

        raise StopIteration
