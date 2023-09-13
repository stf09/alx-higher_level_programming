#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for keys, values in a_dictionary.items():
        new_dict[keys] = 2 * values
    return new_dict
