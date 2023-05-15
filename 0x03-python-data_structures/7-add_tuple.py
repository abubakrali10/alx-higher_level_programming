#!/usr/bin/python3
def add_tuple(tup1, tup2):
    if len(tup1) >= 2 and len(tup2) >= 2:
        sum1 = tup1[0] + tup2[0]
        sum2 = tup1[1] + tup2[1]
    else:
        if len(tup1) < 2:
            tup1 = tup1 + (0,) * (2 - len(tup1))
        if len(tup2) < 2:
            tup2 = tup2 + (0,) * (2 - len(tup2))
        sum1 = tup1[0] + tup2[0]
        sum2 = tup1[1] + tup2[1]
    return (sum1, sum2)
