import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def random_list(length, start, end):
    lst = []
    for i in range(0, length):
        n = random.randint(start, end)
        lst.append(n)
    return lst


def random_matrix(rows, cols, start, end):
    lst = []
    for i in range(0, rows):
        lst.append([])
        for j in range(0, cols):
            lst[i].append(random.randint(start, end))
    return lst


def print_list(list):
    for i in range(len(list)):
        print("%3d" % list[i], end=' ')
    print()


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("%3d" % matrix[i][j], end=' ')
        print()


def get_special(matrix):
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] > st_sum(matrix, i, j) and check_left_and_right(matrix, i, j):
                count += 1
    return count


def st_sum(matrix, i, j):
    sum = 0
    for k in range(0, len(matrix)):
        if i != k:
            sum += matrix[k][j]
    return sum


def check_left_and_right(matrix, i, j):
    result = True
    for k in range(0, len(matrix[i])):
        if k != j:
            if k < j:
                if matrix[i][k] >= matrix[i][j]:
                    result = False
            elif k > j:
                if matrix[i][k] <= matrix[i][j]:
                    result = False
    return result


def convert(lst):
    return [i for item in lst for i in item.split()]


def find_equal_words(lst):
    found = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if lst[i] == lst[j] and found.count(i) == 0 and found.count(j) == 0:
                    print("%s  %s" % (lst[i], lst[j]))
                    found.append(i)
                    found.append(j)


if __name__ == '__main__':
    lst = random_list(10, -60, 60)
    print("Unordered list:")
    print_list(lst)
    insertion_sort(lst)
    print("Ordered list:")
    print_list(lst)
    lst2 = random_matrix(3, 3, -10, 10)
    print("Matrix:")
    print_matrix(lst2)
    print("Count of special elements: %d" % get_special(lst2))
    str = 'one two one'
    print("Given string:")
    print(str)
    str = str.replace(",", "")
    str = [str]
    lst3 = convert(str)
    print("Similar words:")
    find_equal_words(lst3)
