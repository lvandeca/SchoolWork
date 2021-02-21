'''
CIS 210 Python Strings/Counting Substrings

Author: Luke Vandecasteele

Credits: class notes, Bayley

counting the number of slices of a string within a string
'''

def sscount0(needle,haystack):
    '''
    (string,string) -> integer

    This fucntion counts the number of strings (needle)
    within the string (haystack) and then displays that number

    Examples:
    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('!!!', '!!!!!')
    3
    '''
    
    length_h = len(haystack)
    length_n = len(needle)
    counter = 0
    for i in range(length_h):
        dummy = haystack[i:i+length_n]
        if dummy == needle:
            counter += 1
    print(counter)
    return None

def testmod():
    print(doctest.testmod())
    return None
