from datetime import datetime
import time
from random import randint
from functools import wraps

used_functions = list()


def register(func):
    """

    :param func: decorated function
    :return: inner function
    """

    @wraps(func)
    def inner(*args, **kwargs):
        """
        Function adds function`s name to list of used functions
        :param args: list of non-named arguments
        :param kwargs: dictionary of named arguments
        :return: None
        """
        func(*args, **kwargs)
        if hasattr(func, '__wrapped__'):
            used_functions.append(func.__name__)

    return inner


def count_lead_time(func):
    """

    :param func: decorated function
    :return: inner function
    """

    @wraps(func)
    def inner(*args, **kwargs):
        """
        Function counting elapsed time of execution of passed function
        :param args: list of non-named arguments
        :param kwargs: dictionary of named arguments
        :return:
        """
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        time_elapsed: float = (end - start).total_seconds() * 1000
        print(f'>> {func.__name__} passed. Time (ms): {time_elapsed}')

    return inner


def repeat_until_success(func):
    """

    :param func: decorated function
    :return: inner function
    """

    @wraps(func)
    def inner(*args, **kwargs):
        """
        Function will repeat call to passed function until it returns -1
        :param args: list of non-named arguments
        :param kwargs: dictionary of named arguments
        :return: None
        """

        i = 1
        while func(*args, **kwargs) == -1:
            print('Retrying the function...')
            time.sleep(i)
            i += 1

    return inner


@register
@count_lead_time
@repeat_until_success
def random_success_function():
    """
    Test function with 66% chance to return 1
    :return: -1 if number is lower 0 or 1
    """
    number = randint(-1, 1)
    return -1 if number < 0 else 1


def function_with_delay(delay=0):
    """

    :param delay: Delay time in sec
    :return: None
    """
    time.sleep(delay)


if __name__ == '__main__':
    random_success_function()
    function_with_delay = register(count_lead_time(function_with_delay))
    function_with_delay(1)
    print(f"Used functions: {used_functions}")
