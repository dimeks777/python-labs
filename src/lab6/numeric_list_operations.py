from random import randint


def quicksort(lst):
    """
    Returns sorted numerical list
    :param lst: The list to sort
    :return: sorted list or -1 if any element is not int or float
    """
    if check_all_numbers(lst):
        if len(lst) < 2:
            return lst

        low, same, high = [], [], []

        # Select your `pivot` element randomly
        pivot = lst[randint(0, len(lst) - 1)]

        for item in lst:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
        return quicksort(low) + same + quicksort(high)
    return -1


def search_by_value(lst, value):
    """
    Searches element in list by value
    :param lst: List in which searching is used
    :param value: value to search
    :return: value if is found or -1 if in isn`t found or list contains non-numeric values
    """
    if check_all_numbers(lst):
        for i in lst:
            if i == value:
                return i
    return -1


def get_n_minimum_elements(lst, n):
    """
    Gets first n elements with minimum value
    :param lst: List of values
    :param n: Count of elements to get
    :return: List of selected values of -1 if there is 1+ non-numeric value in list
    """
    if check_all_numbers(lst):
        tmp = quicksort(lst)
        return tmp[0:n]
    return -1


def get_n_maximum_elements(lst, n):
    """
    Gets first n elements with maximum value
    :param lst: List of values
    :param n: Count of elements to get
    :return: List of selected values or -1 if there is 1+ non-numeric value in list
    """
    if check_all_numbers(lst):
        tmp = quicksort(lst)
        return tmp[-n:]
    return -1


def get_avg_arithmetical(lst):
    """
    Gets average arithmetical value from list of numeric values
    :param lst: List of values
    :return: Average arithmetical value or None value if there is 1+ non-numeric value in list
    """
    if check_all_numbers(lst):
        return sum(lst) / len(lst)
    return None


def get_unique_list(lst):
    """
    Gets list of unique elements from given list
    :param lst: Given list
    :return: List of unique elements or -1 if there is 1+ non-numeric value in list
    """
    if check_all_numbers(lst):
        return list(set(lst))
    return -1


def get_unique_numbers_list(lst):
    """
    Gets list of unique elements from given list
    :param lst: Given list
    :return: List of unique elements or -1 if there is 1+ non-numeric value in list
    """
    unique = []
    for number in lst:
        if number not in unique:
            unique.append(number)
    return unique


def check_all_numbers(lst):
    """
    Checks if every value in list is numeric
    :param lst: Given list
    :return: True if every value in list is numeric or False if there is 1+ non-numeric value in list
    """
    return all(isinstance(e, (int, float)) for e in lst)
