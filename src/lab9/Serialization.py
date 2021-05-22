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
