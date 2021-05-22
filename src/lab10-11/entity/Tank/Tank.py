from entity.Tank.Tank_modules.Gun import Gun
from entity.Tank.Tank_modules.Hull import Hull
from entity.Tank.Tank_modules.Tower import Tower
from entity.Unit import Unit


class Tank(Unit):
    total_damage = 0

    def __init__(self, name: str, gun: Gun, hull: Hull, tower: Tower):
        self.name = name
        self.gun = gun
        self.hull = hull
        self.tower = tower

    def set_name(self, name: str):
        self.name = name

    def set_gun(self, gun: Gun):
        self.gun = gun

    def set_hull(self, hull: Hull):
        self.hull = hull

    def set_tower(self, tower: Tower):
        self.tower = tower

    def __str__(self):
        return f'Tank: {self.name}\n {self.gun.__str__()}\n {self.hull.__str__()}\n {self.tower.__str__()}'

    def __repr__(self):
        return f'Tank(name={self.name.__repr__()}, gun={self.gun.__repr__()}, hull={self.hull.__repr__()}, ' \
               f'tower={self.tower.__repr__()})'

    def calculate_battle_efficiency(self):
        try:
            return (self.gun.caliber * self.gun.barrel_length) * 0.5 + (
                    self.tower.front + self.tower.side + self.tower.feed) * 0.3 + (
                           self.hull.front + self.hull.side + self.hull.feed) * 0.2
        except TypeError as e:
            print(e)

    def calculate_weight(self):
        try:
            return ((self.tower.front + self.tower.side + self.tower.feed) * 70 + (
                    self.hull.front + self.hull.side + self.hull.feed) * 30) / 1000
        except TypeError as e:
            print(e)

    def damage(self):
        dmg = self.gun.caliber * self.gun.barrel_length
        print(f'Tank damage: {dmg}')
        Tank.total_damage += dmg
        return dmg
