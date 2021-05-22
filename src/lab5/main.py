import copy


def get_distinct_characters(st):
    st = st.replace(" ", "").lower()
    st = st.replace(",", "").lower()

    for letter in st:
        count = string.count(letter)
        if count == 1:
            print("%s" % letter, end=' ')
    print()


def convert_set(set_a):
    set_a.remove('x') if set_a.__contains__('x') else set_a.add('x')
    return set_a


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


def gen_set():
    s1 = set(range(8, 23))
    s2 = set()
    s3 = set()
    for i in range(8, 103):
        s2.add(i) if is_prime(i) else s3.add(i)
    return s1, s2, s3


if __name__ == '__main__':
    string = "aabbcddef qqw nbv, cqw"
    print(f"Unique characters in string:", end=' ')
    get_distinct_characters(string)
    set_a = {1, 'x', 6, 'a', 9}
    tmp_a = copy.deepcopy(set_a)
    set_c = {1, 6, 'a', 9}
    tmp_c = copy.deepcopy(set_c)
    set_b = convert_set(set_a)
    set_d = convert_set(set_c)
    print(f"{tmp_a} -> {set_b}")
    print(f"{tmp_c} -> {set_d}")
    tuple = gen_set()
    print(f"x: {tuple[0]}")
    print(f"y: {tuple[1]}")
    print(f"z: {tuple[2]}")
