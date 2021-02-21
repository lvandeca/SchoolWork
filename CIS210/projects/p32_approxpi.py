'''
CIS 210 Project 3-2 Monte Pi

Author: Luke Vandecasteele

Credits: class notes

This assignment gives an approximation for pi
and compares it to the builtin pi function in
python.
'''

import random
import math

def montePi(numDarts):
    '''
    (integer) -> float

    This function gives an approximation for
    pi by counting the number of points that land
    within the circle and comparing that to the
    total number of points

    Examples:
    >>> montePi(100)
    3.08
    >>> montePi(100000)
    3.143072
    >>> montePi(10000000)
    3.1418752
    '''
    
    inCircle = 0
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        if isInCircle(x,y,1) == True:
            inCircle = inCircle + 1
    pi = inCircle/numDarts * 4

    return pi

def isInCircle(x,y,r):
    '''
    (float,float,float) -> True/False
    
    This function determines whether a point
    (x,y) is within the circle with a radius
    r by using the distance formula

    Examples:
    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    '''
    
    d = math.sqrt(x**2 + y**2)

    if d <= r:
        return True
    else:
        return False

def reportPi(numDarts,approxPi):
    '''
    (integer,float) -> None

    This function compares the builtin function
    pi to our function montePi's approximation
    for pi using the print side effect

    Examples:
    >>> reportPi(1000)
    With 1000 iterations:
    my approximate value for pi is: 3.088
    math lib pi value is: 3.141592653589793
    This is a 1.71 percent error
    >>> reportPi(100000)
    With 100000 iterations:
    my approximate value for pi is: 3.14504
    math lib pi value is: 3.141592653589793
    This is a 0.11 percent error
    '''
    
    print('With', numDarts, 'iterations:')
    answer = montePi(numDarts)
    print('my approximate value for pi is:', answer)
    math_lib_pi_value = math.pi
    print('math lib pi value is:', math_lib_pi_value)
    percent_error = ((abs(math_lib_pi_value - answer))/math_lib_pi_value)*100
    round_percent_error = round(percent_error,2)
    print('This is a', round_percent_error,'percent error')
    return None

def main():
    ''' main driver function for our pi approximation comparison '''
    k = 1000
    mypi = montePi(k)
    reportPi(k,mypi)
    return None
main()
