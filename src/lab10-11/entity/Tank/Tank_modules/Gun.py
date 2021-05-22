from Exceptions.TankExceptions import TankInvalidGunCaliber


class Gun:
    def __init__(self, caliber: int, barrel_length: float):
        if caliber >= 20:
            self.caliber = caliber
            self.barrel_length = barrel_length
        else:
            raise TankInvalidGunCaliber

    def __str__(self):
        return f'Gun caliber: {self.caliber}, barrel length: {self.barrel_length}'

    def __repr__(self):
        return f'Gun(caliber={self.caliber}, barrel_length={self.barrel_length})'
