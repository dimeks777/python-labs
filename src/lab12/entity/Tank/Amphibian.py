from entity.Tank.Tank import Tank
from entity.Tank.Tank_modules.Gun import Gun
from entity.Tank.Tank_modules.Hull import Hull
from entity.Tank.Tank_modules.Tower import Tower


class Amphibian(Tank):
    total_damage = 0

    def __init__(self, name: str, gun: Gun, hull: Hull, tower: Tower, max_depth: float):
        super().__init__(name, gun, hull, tower)
        self.max_depth = max_depth

    def damage(self):
        dmg = self.gun.caliber * self.gun.barrel_length
        print(f'Amphibian damage: {dmg}')
        Amphibian.total_damage += dmg
        return dmg

    def __str__(self):
        return f'Tank: {self.name}\n {self.gun}\n {self.hull}\n {self.tower}\n' \
               f' Max depth: {self.max_depth}'

    def __repr__(self):
        return f'Amphibian(name={self.name.__repr__()}, gun={self.gun.__repr__()}, hull={self.hull.__repr__()}, ' \
               f'tower={self.tower.__repr__()}, max_depth={self.max_depth.__repr__()})'
