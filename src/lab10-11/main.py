from Exceptions.TankExceptions import TankInvalidArmourValueException
from Serialization import write_obj, read_obj
from entity.Tank.Amphibian import Amphibian
from entity.Tank.Tank import Tank
from entity.Tank.Tank_modules.Gun import Gun
from entity.Tank.Tank_modules.Hull import Hull
from entity.Tank.Tank_modules.Tower import Tower


def print_blank_line():
    print('\n-----------------------------------------------------------------------\n')


if __name__ == '__main__':
    try:
        tank = Tank('Tank', Gun(125, 1.8), Hull(1, 200, 100), Tower(350, 250, 200))
    except TankInvalidArmourValueException as e:
        print(e)

# print(tank)
# print_blank_line()
# amphibian = Amphibian('Amphibian', Gun(100, 1.5), Hull(100, 80, 50), Tower(150, 120, 90), 3.5)
# amphibian.damage()
# print(amphibian)
# print_blank_line()
# write_obj(amphibian)
# amphibian2 = eval(read_obj())
# print(amphibian2)
# amphibian2.damage()
# amphibian2.damage()
# amphibian2.damage()
# amphibian2.damage()
# amphibian2.damage()
# print(Amphibian.total_damage)
# Tank.general_info()
