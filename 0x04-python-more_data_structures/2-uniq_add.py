#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    for num in set(my_list):
        sums += num
    return sums
