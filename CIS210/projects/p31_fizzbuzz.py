'''
CIS 210 Project 3-1 Fizzbuzz

Author: Luke Vandecasteele

Credits: Class notes

This function counts inteder numbers starting with one
and replaces numbers divisible by 3 with fizz and
numbers divisible by 5 with buzz and numbers divisible
by both with fizzbuzz
'''

def fb(n):
    '''
    (integer) -> integer/fizz/buzz
    
    This function will count from 1 to n
    and if the counting integer is divisible by 3 it will
    instead display fizz, if the counting integer is divisible by
    5 it will display buzz, and if the integer is divisible
    by 3 and 5 it will display fizzbuzz.
    
    Examples:
    >>> fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    Game over!

    >>> fb(25)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    fizz
    22
    23
    fizz
    buzz
    Game over!
    '''
    counter = 0
    for item in range(n):
        counter += 1
        remainder_3 = counter%3
        remainder_5 = counter%5
        if (remainder_3 == 0) and (remainder_5 ==0):
            print('fizzbuzz')
        elif remainder_5 == 0:
            print('buzz')
        elif remainder_3 == 0:
            print('fizz')
        else:
            print(counter)
    print('Game over!')
    return None
    
            
        
        
