from Exceptions.UnitException import UnitException


class TankInvalidArmourValueException(UnitException):
    def __init__(self, message="Armour can`t be less than 10mm"):
        self.message = message
        super().__init__(self.message)


class TankInvalidGunCaliber(UnitException):
    def __init__(self, message="Caliber can`t be less than 20mm"):
        self.message = message
        super().__init__(self.message)
