#!/usr/bin/python3
def max_integer(my_list=[]):
    c = my_list[0]
    for x in my_list:
       if x > c:
           c = x
    return(c)
