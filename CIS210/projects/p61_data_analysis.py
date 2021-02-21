'''
CIS 210: Data Analysis

Author: Luke Vandecasteele

Credits: Class notes, textbook

This funtion is used to test mean, median,
and mode functions by also generating a
frequency table and using these functions
to analyze a bunch of earthquake data.
'''

import doctest

def mean(alist):
    '''
    (list) -> float

    This function gives the mean
    or average of a list of numbers
    (alist).

    >>> mean([20,32,21,26,33,22,18])
    24.571428571428573

    >>> mean([1])
    1.0
    '''
    
    mean = sum(alist) / len(alist)
    return mean

def median(alist):
    '''
    (list) -> float

    This function finds the middle
    number of a set of data (alist)
    after being listed in numerical
    order.

    Calls isEven()

    >>> median([20,32,21,26,33,22,18])
    22
    
    >>> median([0])
    0
    '''
    
    copylist = alist[:]
    copylist.sort()
    len_copylist = len(copylist)
    
    if isEven(len_copylist):
        rightmid = len_copylist//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:
        mid = len_copylist//2
        median = copylist[mid]
    return median

def mode(alist):
    '''
    (list) -> float

    This function determines which number
    in a set of data (alist) occurs
    most frequently.

    >>> mode([1,1,4,5,6,2,4,7,1,4,6,1])
    [1]

    >>> mode([3])
    [3]

    '''
    countdict = genFrequencyTable(alist)
    countlist = countdict.values()
    maxcount = max(countlist)

    modelist = [ ]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)

    return modelist

def frequencyTable(alist):
    '''
    (list) -> None

    This function generates a table
    based of a list (alist) of data
    and gives each item in the list
    and how many times they occur
    in the list.

    >>> frequencyTable([1,1,1,1,1,2,2,2,3,3,4,5])
    Item Frequency
    1     5
    2     3
    3     2
    4     1
    5     1

    >>> frequencyTable([1])
    Item Frequency
    1     1
    
    '''
    countdict = genFrequencyTable(alist)
    itemlist = list(countdict.keys())
    itemlist.sort()

    print('Item','Frequency')

    for item in itemlist:
        print(item, '   ', countdict[item])
        
    return None

def isEven(n):
    '''
    (int) -> Boolean

    This function determines if
    an integer (n) is even.

    >>> isEven(0)
    True
    
    >>> isEven(3)
    False
    '''
    
    if n%2 ==0:
        return True
    else:
        return False

def genFrequencyTable(alist):
    '''
    (list) -> dictionary

    This function takes a list
    (alist) and determines how frequently
    each item in the list occurs. It
    then returns a dictionary which associates
    each number with the number of times it
    occurs in the list.

    >>> genFrequencyTable([1,2,1,2,3,2])
    {1: 2, 2: 3, 3: 1}

    >>> genFrequencyTable([])
    {}
    '''
    countdict = {}
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1
    return countdict

def main():
    '''
    Main program driver function
    '''
    
    equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
    2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
    4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
    4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
    2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
    4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
    3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
    2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
    2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
    6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
    2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
    2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
    4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
    4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
    2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
    2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
    2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
    4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
    4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
    2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
    3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
    2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
    2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
    2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
    2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
    2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
    3.1, 4.6, 2.8, 3.1, 6.3]

    equakes_mean = mean(equakes)
    equakes_median = median(equakes)
    equakes_mode = mode(equakes)

    print('Earthquake Magnitude Data Analysis:')
    equakes_frequency = frequencyTable(equakes)
    print('The mean is:', equakes_mean)
    print('The median is:', equakes_median)
    print('The mode is:', equakes_mode)

    return None

doctest.testmod()

if __name__ == '__main__':
    main()
