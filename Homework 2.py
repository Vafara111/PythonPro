def get_lenght(text : str) -> int:
    return len(text)

def concatenate(str1: str, str2: str) -> str:
    return str1 + " " + str2

def square(number: int) -> int:
    return number ** 2

def sum(number1: int, number2: int) -> int:
    return number1 + number2

def divide(number1: int, number2: int) -> tuple:
    return divmod(number1, number2)

def average(lst: list) -> int:
    av = 0
    for number in lst:
        av += number
    return av / len(lst)

def intersection(lst1: list, lst2: list) -> list:
    return list(set(lst1).intersection(lst2))

def keys(dictionary: dict) -> list:
    return list(dictionary.keys())

def dict_sum(dict1: dict, dict2: dict) -> dict:
    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3

def set_sum(set1: set, set2: set) -> set:
    return set1.union(set2)

def is_subset(set1: set, subset: set) -> bool:
    if subset.issubset(set1):
        return True
    return False

def is_pair(number: int) -> str:
    if number % 2 == 0:
        return "Pair"
    return "Not pair"

def pair_list(lst: list) -> list:
    new_list = []
    for number in lst:
        if number % 2 == 0:
            new_list.append(number)
    return new_list
