import contextlib
from entity.Tank.Tank import Tank
from entity.Tank.Tank_modules.Gun import Gun
from entity.Tank.Tank_modules.Hull import Hull
from entity.Tank.Tank_modules.Tower import Tower
from entity.Tank.Amphibian import Amphibian


def write_obj(obj, file_name='default.txt'):
    try:
        file = open(file_name, 'w')
        file.write(obj.__repr__())
        file.close()
    except IOError as e:
        print(e)


def read_obj(file_name='default.txt'):
    try:
        file = open(file_name, 'r')
        obj = file.read()
        file.close()
        return obj
    except IOError as e:
        print(e)


@contextlib.contextmanager
def read_objects(path_to_file):
    file = open(path_to_file, 'r')
    content = file.readlines()
    yield [eval(x) for x in content]
    file.close()
