#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set()
    sum = 0
    for a in range(len(my_list)):
        if my_list[a] not in unique_elements:
            sum = sum + my_list[a]
            unique_elements.add(my_list[a])
    return sum
