from math import sqrt

def myDist(P1,P2):
    '''
    (list,list) -> float

    Takes two points (P1,P2) in the form of lists
    and returns the distance between the two points.

    >>> myDist([0,3],[4,0])
    5.0
    >>> myDist([0,0],[0,0])
    0.0
    >>> myDist([4.2,3],[6.7,1])
    3.2015621187164243
    '''
    
    distance = sqrt(((P2[0] - P1[0]) ** 2) + (P2[1] - P1[1]) ** 2)
    return distance

def isIn(point):
    '''
    (list) -> Boolean

    Calculates if a point (point) is inside
    a circle with radius 1.

    >>> isIn([0,1])
    True
    >>> isIn([1,1])
    False
    >>> isIn([0,0])
    True
    '''
    
    distance_to_origin = myDist([0,0], point)
    if distance_to_origin <= 1:
        return True
    else:
        return False



def my_fun(astring):

    symbols = ['@', '#', '$']
    symbols_ctr = 0

    for c in astring:
        if c in symbols:
            symbols_ctr += 1

    return (symbols_ctr >= 2)


def foo(astr):
    myD = {}
    for ch in astr:
        if ch in myD:
            myD[ch] += 1
        else:
            myD[ch] = 1
        print(myD)

    valL = myD.values()
    ct = min(valL)

    myS = []
    for item in myD:
        if myD[item] == ct:
            myS.append(item)
        print(myS)
        
    return myS

myStr = 'hhhjjjkmmmm'

    
