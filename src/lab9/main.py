from Serialization import write_obj, read_obj
from Tank import Tank, Gun, Hull, Tower

if __name__ == '__main__':
    tank = Tank('T-90', Gun(125, 1.8), Hull(250, 200, 100), Tower(350, 250, 200))
    print(tank)
    tank2 = eval(repr(tank))
    print(f'Battle efficiency of {tank.name} is {tank.calculate_battle_efficiency()}')
    print(f'Weight of {tank.name} is {tank2.calculate_weight()}')
    write_obj(tank)
    print(eval(read_obj()))