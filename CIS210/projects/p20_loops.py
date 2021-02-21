'''
Learning Looping
CIS 210 Project 2-0 For Loops

Author: Luke Vandecasteele

Credits: Class Notes

Practice writing for loops in python
and comparing them to while loops
'''

def q6_better():
    '''
    -() -> int
    -Return 2 to the power of 4.
    -Example:
    >>> q6()
    16
    '''
    i = 0
    p = 1
    for i in range(4):
        p = p * 2
        i += 1
    return p

def q6_final(n,m):
    '''
    -(float,int) -> float
    -This function takes any float (n) and raises
    it to the (m) power.
    -Examples:
    >>> q6_final(5,3)
    125
    >>> q6_final(2,4)
    16
    '''
    i = 0
    p = 1
    for i in range(m):
        p = p * n
        i += 1
    return p

def add_digits2a_better(n):
    '''(int) --> int

    Return sum of digits of n, a positive 3-digit integer.
    Implement using a while loop.

    >>> add_digits2a_better(789)
    24
    >>> add_digits2a_better(101)
    2
    >>> add_digits2a_better(000)
    0
    '''
    digit_sum = 0
    ctr = 1
    for ctr in range(3):
        digit = n % 10
        n = n // 10
        digit_sum += digit
        ctr += 1
    return digit_sum

def add_digits2b_better(n):
    '''(int) --> int

    Return sum of digits of n, where n is a
    positive integer of any length.

    >>> add_digits2b_better(789)
    24
    >>> add_digits2b_better(101)
    2
    >>> add_digits2b_better(000)
    0
    >>> add_digits2b_better(5)
    5
    >>> add_digits2b_better(10101)
    3
    '''
    digit_sum = 0
    for stop in range(n):
        if n >= 0:
            digit = n % 10
            n = n // 10
            digit_sum += digit

    return digit_sum

# This is not a good approach to add a "for" loop
# for the function add_digits2b_better(n) because
# you basically have to add the same thing in the next
# line in an if statement in order for the "for" loop to work
