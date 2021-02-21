''' 
Prior programming experience quiz.
CIS 210 W20 Project 1-1 Hello-Quiz Solution

Author: Luke Vandecasteele

Credits: class notes

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket.py for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''
    docstring -
    - (True/False,True/False) -> greeting
    - This function displays the appropriate greeting depending
    upon whether a person arrives on time, late, or is absent
    - Examples of function:
    >>> q1(True,False)
    'Hello!'
    >>> q1(False,True)
    'Is anyone there?'
    >>> q1(False,False)
    'Better late than never.'
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''
    docstring -
    - (number,number) -> True/False
    - This function determines whether a person is dependent
    or not. If the person is under 18 and makes less than 10000
    than it returns true beause they are dependent. Otherwise it
    returns false.
    - Examples:
    >>> q2(17,120000)
    False
    >>> q2(27,9000)
    False
    >>> q2(9,100)
    True
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''
    docstring -
    - () -> 6 
    - This function follows an algorithm that always gives
    an output of 6 because the function does not allow inputs
    and so p and q will never change values always resulting
    in 6.
    - Examples:
    >>> q3()
    6
    >>> q3()
    6
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''
    docstring -
    - (float,float) -> float
    - This function is used to calculate the balance
    of an account with a desposit up to 10 times
    - Examples:
    >>> q4(100,10)
    200
    >>> q4(10,10)
    110
    >>> q4(11.1,4.4)
    55.09999999999999
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''
    docstring -
    (list of numbers) -> number       
 
    - This function counts and produces the number of numbers greater
    than or equal to in list.

    >>> q5([0, 1, 2, 3, 4, 5])    
    6
    >>> q5([0, -1, 2, -3, 4, -5])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''
    docstring -
    - () -> 12
    - This function's algorithm returns 16 everytime because the function
    has no operation within it to allow for differing input values. Accordingly
    it does 2**4 
    -Examples:
    >>> q6()
    16
    '''
    i = 0
    p = 1
    while i < 4:
        p = p * 2
        i += 1

    return p
