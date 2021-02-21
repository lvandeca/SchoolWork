'''
CIS 210: Binary Search

Author: Luke Vandecasteele

Credits: class notes

This function determines if a sorted
sequence contains a target value
by a iterative method as well as a
recursive method and then checks the
fucntion outputs to make sure they
are correct.
'''


def isMemberI(aseq, target):
    '''
    (sequence, item) -> Boolean

    This function uses sequential search
    to determine if an item (target)
    is in a sort list (sequence) and return
    True if the target is in aseq, and False
    if it is not

    >>> isMemberI((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberI((1, 2, 3, 3, 4), 2)
    False
    >>> isMemberI('aeiou', 'i')
    True
    >>> isMemberI('aeiou', 'y')
    False
    '''
    for item in aseq:
        if item == target:
            return True
    return False

def isMemberR(aseq, target):
    '''
    (sequence, item) -> Boolean

    Use binary search to check for membership
    of int n in sorted sequence, seq. Return
    True if n is a member, else return False.
    (recursive implementation)
    
    >>> isMemberR((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberR((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberR('aeiou', 'i')
    True
    >>> isMemberR('aeiou', 'y')
    False
    '''

    mode_aseq = len(aseq) // 2
    if len(aseq)  == 0:
        return False
    else:
        if aseq[mode_aseq] == target:
            return True
        else:
            if aseq[mode_aseq] > target:
                return isMemberR(aseq[0: mode_aseq - 1], target)
            else:
                return isMemberR(aseq[mode_aseq + 1: len(aseq)],target)

def bintest(f):
    if f == isMemberR:
        print(isMemberR((1, 2, 3, 3, 4), 3))
        print(isMemberR((1, 2, 3, 3, 4), 99))
        print(isMemberR('aeiou', 'i'))
        print(isMemberR('aeiou', 'y'))
        print(isMemberR((1, 3, 5, 7), 4))
        print(isMemberR((23, 24, 25, 26, 27), 5))
        return None
            
