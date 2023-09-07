#!/usr/bin/python3
import hidden_4


def discovr():
    name = dir(hidden_4)
    for k in name:
        if k[:2] != '__':
            print("{:s}".format(k))


if __name__ == "__main__":
    discovr()
