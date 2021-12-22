#!/bin/python3
def findDigits(n):
    return sum(char != "0" and n % int(char) == 0 for char in str(n))
