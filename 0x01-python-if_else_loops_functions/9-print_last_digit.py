#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_di = number % -(10)
        print(-(last_di), end='')
    else:
        last_di = number % 10
        print(last_di, end='')
    return abs(last_di)
