class UnitException(Exception):
    def __init__(self, message="Default exception message"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'