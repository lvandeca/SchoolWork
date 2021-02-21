f"""
CIS 211: Week 2

Author: Luke Vandecasteele

Credits: class notes

Practice on for loops and iterating
through a list.
"""


def all_same(l: list) -> bool:
    if len(l) == 0:
        return True
    else:
        init_object = l[0]
        for item in l:
            if item != init_object:
                return False
        return True


def dedup(l: list) -> list:
    return_list = [ ]
    for item in l:
        if item not in(return_list):
            return_list.append(item)
    return return_list


def max_run(l: list) -> int:
    max_count = 1
    len_l = len(l)
    if len_l == 0:
        return 0
    for item in range(len_l - 1):
        i = item + 1
        current_count = 1
        while i <= (len_l - 1):
            if l[item] == l[i]:
                current_count += 1
                i += 1
            else:
                break
        if current_count > max_count:
            max_count = current_count
    return max_count



