from Exceptions.TankExceptions import TankInvalidArmourValueException
from entity.Tank.Tank_modules.Hull import check_armour_value


class Tower:
    def __init__(self, front: int, side: int, feed: int):
        if check_armour_value(front, side, feed):
            self.front = front
            self.side = side
            self.feed = feed
        else:
            raise TankInvalidArmourValueException

    def __str__(self):
        return f'Tower armour: front: {self.front}, side: {self.side}, feed: {self.feed}'

    def __repr__(self):
        return f'Tower(front={self.front}, side={self.side}, feed={self.feed})'
