#!/usr/bin/env python
# Prints out the first n values of the Fibonacci sequence
import sys

def fib(n=10, a=1, b=1):
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c



if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = None
    fib(n)
