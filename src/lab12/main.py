from typing import List

from Serialization import read_objects
from entity.Tank.Amphibian import Amphibian
from entity.Tank.AmphibianDivision import AmphibianDivision
from entity.Tank.Tank import Tank
from entity.Tank.TankDivision import TankDivision
from entity.Tank.Tank_modules.Gun import Gun
from entity.Tank.Tank_modules.Hull import Hull
from entity.Tank.Tank_modules.Tower import Tower


def print_blank_line():
    print('\n-----------------------------------------------------------------------\n')


if __name__ == '__main__':
    tank = Tank('Tank', Gun(125, 1.8), Hull(250, 200, 100), Tower(350, 250, 200))
    print_blank_line()
    amphibian = Amphibian('Amphibian', Gun(100, 1.5), Hull(100, 80, 50), Tower(150, 120, 90), 3.5)
    a: List[Tank] = list([tank, amphibian, tank])
    t = TankDivision([tank, amphibian, tank])
    iterator = iter(t)
    while True:
        try:
            elem = next(iterator)
            # print(elem)
        except StopIteration:
            break

    tt = AmphibianDivision([amphibian, amphibian, amphibian])
    generator = tt.get_troops(2)
    print(next(generator))

    with read_objects("default.txt") as objects:
        division = AmphibianDivision(objects)
        print(division.tanks.pop(0))
