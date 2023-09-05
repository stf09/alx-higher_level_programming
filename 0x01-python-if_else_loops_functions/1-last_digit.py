#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number[:-1]
if last_digit > 5:
  ss = "and is greater than 5"
elif last_digit == 0:
  ss = "and is 0"
elif last_digit < 6 and last_digit != 0:
  ss = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {s}")
