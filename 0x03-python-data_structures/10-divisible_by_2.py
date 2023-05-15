#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_by_2_list = []
    for i in my_list:
        if i % 2 == 0:
            divisible_by_2_list.append(True)
        else:
            divisible_by_2_list.append(False)
    return divisible_by_2_list
