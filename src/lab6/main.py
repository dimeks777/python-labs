from datetime import datetime
from math import ceil

from numeric_list_operations import search_by_value, quicksort, get_n_minimum_elements, get_n_maximum_elements, \
    get_avg_arithmetical, get_unique_list


def get_century(year=datetime.now().year):
    """
    Returns century value for given year
    :param year: Giver year, by default it is current year
    :return: Number of century which year belongs to
    """
    if isinstance(year, int):
        return ceil(year / 100)


if __name__ == '__main__':
    l = [1, 7, 2, 3, 3]
    print(f"Searching value 7: {search_by_value(l, 7)}")
    print(f"Sorted list: {quicksort(l)}")
    print(f"First 3 elements: {get_n_minimum_elements(l, 3)}")
    print(f"Last 3 elements: {get_n_maximum_elements(l, 3)}")
    print(f"Average arithmetical: {get_avg_arithmetical(l)}")
    print(f"List of unique elements: {get_unique_list(l)}")
    print(f"Century of 2011 year: {get_century(2011)}")
