def file_read_write(func, path='resources/default.txt', mode='r', **kwargs):
    """

    :param func: funnction to execute with file
    :param path: path to source file
    :param mode: mode for file open
    :param kwargs: named args for func
    :return: None
    """
    try:
        source = open(path, mode)
        func(source, **kwargs)
        source.close()
    except IOError as e:
        print(e)


def rewrite(source, c1='a', c2='o', dest='resources/1.txt'):
    """

    :param source: source file
    :param c1: symbol to change
    :param c2: changed symbol
    :param dest: destination file
    :return: None
    """
    content = source.readlines()
    result = [st.replace(c1, c2) for st in content]
    with open(dest, 'w') as dst:
        dst.writelines(result)


def even_odd_write(source, dest1, dest2):
    """

    :param source: source file
    :param dest1: first destination file
    :param dest2: second destination file
    :return: None
    """
    content = source.readlines()
    with open(dest1, 'w') as dst:
        dst.writelines(content[::2])
    with open(dest2, 'w') as dst:
        dst.writelines(content[1::2])


if __name__ == '__main__':
    file_read_write(rewrite, c1='o', c2='a')
    file_read_write(even_odd_write, dest1='resources/2.txt', dest2='resources/3.txt')
