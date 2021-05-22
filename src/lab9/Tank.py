class Tank:

    def __init__(self, name, gun, hull, tower):
        self.name = name
        self.gun = gun
        self.hull = hull
        self.tower = tower

    def __str__(self):
        return f'Tank: {self.name}\n {self.gun.__str__()}\n {self.hull.__str__()}\n {self.tower.__str__()}'

    def __repr__(self):
        return f'Tank(name={self.name.__repr__()}, gun={self.gun.__repr__()}, hull={self.hull.__repr__()}, tower={self.tower.__repr__()})'

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


class Gun:
    def __init__(self, caliber, barrel_length):
        self.caliber = caliber
        self.barrel_length = barrel_length

    def __str__(self):
        return f'Gun caliber: {self.caliber}, barrel length: {self.barrel_length}'

    def __repr__(self):
        return f'Gun(caliber={self.caliber}, barrel_length={self.barrel_length})'


class Hull:
    def __init__(self, front, side, feed):
        self.front = front
        self.side = side
        self.feed = feed

    def __str__(self):
        return f'Hull armour: front: {self.front}, side: {self.side}, feed: {self.feed}'

    def __repr__(self):
        return f'Hull(front={self.front}, side={self.side}, feed={self.feed})'


class Tower:
    def __init__(self, front, side, feed):
        self.front = front
        self.side = side
        self.feed = feed

    def __str__(self):
        return f'Tower armour: front: {self.front}, side: {self.side}, feed: {self.feed}'

    def __repr__(self):
        return f'Tower(front={self.front}, side={self.side}, feed={self.feed})'
