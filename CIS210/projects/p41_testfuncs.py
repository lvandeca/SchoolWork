'''
CIS 210 Test Function

Author: Luke Vandecasteele

Credits: Class notes

This function is used to test various functions including all
the edge cases to see if it operates as expected
'''

def test_sscount(f,args,expected_result):
    '''
    (function,string,integer) -> None

    This function is to test the sscount0 function as well as
    the sscount1 function and make sure the the expected result
    is what our actual result is from the function.

    Examples:
    testing sscount0
    checking needle  haystack ...
    its value 0 is correct!
    testing sscount0
    checking needle  haystack
    its value 0 is correct!

    testing sscount0
    checking !!!  !!!!! ...
    its value 3 is correct!
    testing sscount0
    checking !!!  !!!!!
    its value 3 is correct!
    '''
    len_args = len(args)
    needle = ''
    haystack = ''
    for item in range(len_args):
        if args[item] == ' ':
            needle = args[0:item]
            haystack = args[item:len_args]
    if f == sscount0:
        answer0 = sscount0(needle,haystack)
        print('testing sscount0')
        print('checking', needle, haystack,'...')
        if expected_result == answer0:
            print('its value', expected_result, 'is correct!')
        else:
            print('its value', expected_result, 'is incorrect.')
    if f == sscount1:
        answer1 = sscount1(needle,haystack)
        print('testing sscount0')
        print('checking', needle, haystack)
        if expected_result == answer1:
            print('its value', expected_result, 'is correct!')
        else:
            print('its value', expected_result, 'is incorrect.')
    return None

import doctest

def sscount0 (needle, haystack):
    '''(str, str) -> int

    Given a "needle" string to search for in a "haystack" string,
    return the count of the number occurrences of the needle in
    the haystack.  Overlapping substrings are included.
    Uses string slice operation (only).
    
    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('an', 'trans-Panamanian banana')
    6
    >>> sscount0('needle', 'haystack')
    0
    >>> sscount0('!!!', '!!!!!')
    3
    >>> sscount0('o', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    9
    '''
    ctr = 0
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+n] == needle:
            ctr += 1
    return ctr

def sscount1 (needle, haystack):
    '''(str, str) -> int

    Given a "needle" string to search for in a "haystack" string,
    return the count of the number occurrences of the needle in
    the haystack.  Overlapping substrings are included.
    Using string startswith method simplifies code a bit.
    
    >>> sscount1('sses', 'assesses')
    2
    >>> sscount1('an', 'trans-Panamanian banana')
    6
    >>> sscount1('needle', 'haystack')
    0
    >>> sscount1('!!!', '!!!!!')
    3
    >>> sscount1('o', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    9
    '''
    ctr = 0
    for i in range(len(haystack)):
        if haystack[i:].startswith(needle):
            ctr += 1
    return ctr

def main():
    '''test for test_sscount() function '''
    test_sscount(sscount0,'sses assesses',2)
    test_sscount(sscount1,'sses assesses',2)
    print('')
    test_sscount(sscount0,'an trans-Panamanian banana',6)
    test_sscount(sscount1,'an trans-Panamanian banana',6)
    print('')
    test_sscount(sscount0,'needle haystack',0)
    test_sscount(sscount1,'needle haystack',0)
    print('')
    test_sscount(sscount0,'!!! !!!!!', 3)
    test_sscount(sscount1,'!!! !!!!!', 3)
    print('')
    test_sscount(sscount0,'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount(sscount1,'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    print('')
    test_sscount(sscount0,'', 0)
    test_sscount(sscount1,'', 0)
    print('')
    test_sscount(sscount0,'a ', 0)
    test_sscount(sscount1,'a ', 0)
    print('')
    test_sscount(sscount0,' abc', 0)
    test_sscount(sscount1,' abc', 0)
    print('')
    test_sscount(sscount0,'a a', 1)
    test_sscount(sscount1,'a a', 1)
    return None

main()
