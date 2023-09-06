#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    if a % 2 == 0:
        f = 0
    else:
        f = 32
    print('{}'.format(chr(a - f)), end='')
