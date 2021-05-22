from Exceptions.TankExceptions import TankInvalidArmourValueException


def check_armour_value(front, side, feed):
    if front >= 10 and side >= 10 and feed >= 10:
        return True
    else:
        return False


class Hull:
    def __init__(self, front: int, side: int, feed: int):
        if check_armour_value(front, side, feed):
            self.front = front
            self.side = side
            self.feed = feed
        else:
            raise TankInvalidArmourValueException

    def __str__(self):
        return f'Hull armour: front: {self.front}, side: {self.side}, feed: {self.feed}'

    def __repr__(self):
        return f'Hull(front={self.front}, side={self.side}, feed={self.feed})'
