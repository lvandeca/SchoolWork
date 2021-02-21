'''
Babylonian Approximation for Square Roots
CIS 210 Project 2-2 Square Root

Author: Luke Vandecasteele

Credits: Class notes

Approximate square roots and compare them to
the math.sqrt() function builtin to python
'''

from math import *

def main():
    '''Square root comparison program driver.'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()

def sqrt_compare(num,iterations):
    '''
    - (float,int) -> None
    - This function compares the python builtin square root
    function to the Babylonian approximation of a square root.
    The number (num) we want to square is put into both functions
    and (iterations) is put into the approximation to determine
    how many steps we want for our approximation.
    - Examples:
    >>> sqrt_compare(10000, 8)
    For  10000 using 8 iterations:
    mysqrt value is:  101.20218365353946
    math lib sqrt value is:  100.0
    This is a 1.2 percent error.
    >>> sqrt_compare(625,5)
    For 625 using 5 iterations
    mysqrt value is: 29.1828724815876
    math lib sqrt value is: 25.0
    This is a 16.73 percent error
    '''
    print('For', num, 'using', iterations, 'iterations')
    answer = mysqrt(num,iterations)
    print('mysqrt value is:', answer)
    math_lib_sqrt = sqrt(num)
    print('math lib sqrt value is:', math_lib_sqrt)
    percent_error = ((abs(math_lib_sqrt - answer))/math_lib_sqrt)*100
    round_percent_error = round(percent_error,2)
    print('This is a', round_percent_error, 'percent error')
    return None

def mysqrt(n,k):
    '''
    - (float,int) -> float
    - This function approximates the square root of a
    positive number n, using the Babylonian method. The
    function runs the algorithm k times which, as k increases,
    the approximation gets more accurate.
    - Examples:
    >>> mysqrt(25, 5)
    5.000023178253949
    >>> mysqrt(25, 10)
    5.0
    >>> mysqrt(100, 10)
    10.0
    >>> mysqrt(625, 5)
    29.1828724815876
    '''
    x = 1
    for item in range(k):
        item = n
        x = .5*(x + item/x)
    return x





    
