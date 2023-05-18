#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score_value = 0
    best_score_key = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > best_score_value:
            best_score_value = a_dictionary[key]
            best_score_key = key
    return best_score_key
