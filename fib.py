import sys
from math import sqrt

# 
# Compute the N'th Fibonacci number 1 1 2 3 5 8 13 21 34 55 89 144
#
#                                   0 1 2 3 4 5  6  7  8  9 10  11

# Finding the nth fibonacci number recursively
def fib(n):
    if n == 0 or n == 1:
       return 1
    else:
       return fib(n-1) + fib(n-2)

# Finding the nth fibonacci number recursively
def fib2(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return fib2(n-1) + fib2(n-2)   

# Finding the nth fibonacci number iteratively
def f(n):
    a = 1
    b = 1 
    for i in range(n):
        a,b = b,a+b 
    return a

print f(10)
 

