'''
CIS W20 Project 1-2: Python Variations

Author: Luke Vandecasteele

Credits: class text notes

Various number manipulations in python
'''

def convert(i,j,k):
    '''
docstring:
-(number,number,number) -> number
-This function combines three numbers to create one
number where 0<=i,j,k<=0 and i is the least significant
dijit and k the most significant
-Examples:
>>> convert(1,2,3)
321
>>> convert(0,0,1)
100
>>> convert(1,0,0)
1
 >>> convert(0,0,0)
0
'''
    
    return int(f"{k}{j}{i}")

def add_digits(n):
    '''
    -(number) -> number
    - This function adds the digits of a three digit number
    -Examples:
    >>> add_digits2(155)
    11
    >>> add_digits2(122)
    5 '''
    result = 0
    while n > 0:
        rem = n % 10
        result = result + rem
        n = int(n/10)
    return result

def add_digits2(n):
    '''
    -(number) -> number
    - This function adds all the digits in an integer
    -Examples:
    >>> add_digits2(155)
    11
    >>> add_digits2(12)
    3 '''
    result = 0
    while n > 0:
        rem = n % 10
        result = result + rem
        n = int(n/10)
    return result

def profit(x):
    '''
    -(number) -> float
    -This function calculates the net profit of a theater
based on the number of customers in the theater.
-Examples:
>>> profit(10)
2.5
>>> profit(10)
25.0
>>> profit(0)
-20.0
'''
    cost = 20
    customer = 5
    costpercustomer = 0.5
    _numbcust = x

    while _numbcust >=0:
        money = _numbcust*customer -_numbcust*0.5 - 20
        return money

    


