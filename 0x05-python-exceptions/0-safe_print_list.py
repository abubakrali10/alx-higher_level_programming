#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nums = 0
    for el in range(x):
        try:
            print(f"{my_list[el]}", end="")
            nums = nums + 1
        except IndexError:
            break
    print("")
    return nums
