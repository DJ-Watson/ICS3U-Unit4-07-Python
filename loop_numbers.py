#!/usr/bin/env python3

# Created by DJ Watson
# Created on November 2019
# this program prints all  numbers from 1000-2000 with 5 numbers a line


def main():
    loop_c = 1

    for num in range(1000, 2001):
        loop_c += 1
        if loop_c % 5 == 1:
            print("{} ".format(num))
        else:
            print("{} ".format(num), end="")


if __name__ == "__main__":
    main()
