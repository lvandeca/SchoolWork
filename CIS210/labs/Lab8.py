def btod_type(bin_str):

    assert isinstance(bin_str,str) #helps to encourage a type
                                   #contract by checking that your
                                   #input follows what you want for your funtion
    print('Your string is ' + bin_str)
    return None

def btod_bits(bin_str):

    for bit in bin_str:
        assert bit in ['0','1'], 'A binary number is needed'
        # the string at the end helps describe why your assertion error is wrong
    print('Your string is ' + bin_str)
    return None
#assert isnt used that much, dont want to litter code with assert
#statements

def divByZero():
    try:
        x = 1/0
    except:
        print('Tried to divide by zero')

    return None

def divByZero():
    try:
        x = 1/0
    except ZeroDivisionError:
        print('Tried to divide by zero')

    return None

#try and except are much better because they provide
#more specific examples for your errors
#can define your own errors for functions with this try and except stuff

def double_your_num(n):
    assert isinstance(n,int), 'Please enter an integer'
    assert n in [1,2,3,4,5,6,7,8,9,10], 'Integer not between 1 and 10'

    print('Double your number is:', n*2)
    return None

#Given the following python code
#to increment the first n integers
#in a list of integers by one:

def incr_li(li,n):
    '''(list of ints, int) -> None

    Increment the first n values in
    a list by 1 and print the new list.

    >>> incr_li([1,2,3,4], 2)
    [2, 3, 3, 4]

    >>> incr_li([1, 2, 3, 4], 5)
    [2, 3, 4, 5]
    '''

    try:
        newli = li[:]       #slicing the entire list creates a copy
        for i in range(n):
            newli[i] += 1
        print(newli)

    except:
        if IndexError:
            print('Error: The list index is out of range.')

    return None
    
