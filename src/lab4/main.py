import collections
import math

def has_more_than_two_items(dic):
    count = 0
    for i in dic:
        if dic.get(i)[0] > 2:
            count += 1
    return count


def has_one_item_less_25kg(dic):
    for i in dic:
        baggage = dic.get(i)
        if baggage[0] == 1 and baggage[1] < 25:
            return True
    return False


def average_item_count(dic):
    sum = 0
    for i in dic:
        sum += dic.get(i)[0]
    return sum / len(dic)


def avg_item_weight(dic):
    sum = 0
    for i in dic:
        baggage = dic.get(i)
        sum += baggage[1] / baggage[0]
    return sum / len(dic)


def number_of_baggage_weight_in_delta(dic):
    avg = avg_item_weight(dic)
    print(f"Average item weight: {avg.__round__(2)}")
    index = 1
    for i in dic:
        baggage = dic.get(i)
        curAvg = baggage[1] / baggage[0]
        if math.fabs(curAvg - avg) <= 0.5:
            return index
        index += 1
    return -1


def has_items_more_than_average(dic):
    avg = average_item_count(dic)
    print(f"Average item count: {avg.__round__(2)}")
    count = 0
    for i in dic:
        if dic.get(i)[0] > avg:
            count += 1
    return count


def print_dictionary(dic):
    i = 1
    for k, v in dic.items():
        print(f"{i}. {k} -  Items:{v[0]} Weight: {v[1]}")
        i += 1


def add_to_dict(dic, name, count, total_weight):
    dic.update({name: (count, total_weight)})
    return dic


def get_sorted_dict(dic):
    return collections.OrderedDict(sorted(dic.items()))


if __name__ == '__main__':
    dic = {
        "John": (1, 2.5),
        "Alex": (3, 0.5),
        "Dasha": (1, 3.1),
        "Elizabeth": (7, 5.75),
        "Sergio": (4, 2.2),
        "Dmitriy": (2, 0.93),
        "Daniil": (8, 8.8),
        "Ivan": (1, 7.5),
        "Pavel": (1, 1.4),
        "Victoria": (11, 10.1)
    }
    dic = add_to_dict(dic, 'Lexa', 1, 1.0)
    print("Unordered dictionary:")
    print_dictionary(dic)
    dic = get_sorted_dict(dic)
    print("Ordered dictionary:")
    print_dictionary(dic)
    print(f"Count of passengers that has more than 2 items: {has_more_than_two_items(dic)}")
    print(f"Is any passenger have only 1 item that has weight below 25 kg? : {has_one_item_less_25kg(dic)}")
    print(f"Count of passengers with item count more tnan average: {has_items_more_than_average(dic)}")
    print(f"Index of baggage which weight is in range 0.5 from average {number_of_baggage_weight_in_delta(dic)}")
