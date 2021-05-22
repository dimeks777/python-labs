# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from cmath import sin


def calculate_expression(alpha):
    return 1 / 4 - 1 / 4 * sin(5 / 2 * math.pi - 8 * alpha)


def sum_n(n, k):
    tmp = 1
    result = 0
    while tmp <= n:
        if tmp % k == 0:
            result += tmp
        tmp += 1
    return result


if __name__ == '__main__':
    try:
        n1 = input("Enter n\n")
        n1 = int(n1)
        k1 = input("Enter k\n")
        k1 = int(k1)
        print("k should not be zero\n") if k1 == 0 else print(sum_n(n1, k1))
        alpha1 = input("Enter alpha\n")
        alpha1 = int(alpha1)
        print(calculate_expression(alpha1))
    except ValueError:
        print("Enter a decimal numbers\n")
