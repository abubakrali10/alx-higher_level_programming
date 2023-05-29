#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nums = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            nums = nums + 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print("")
    return nums
