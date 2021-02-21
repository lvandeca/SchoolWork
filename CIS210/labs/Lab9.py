import pdp.py

def createTempD(days,temps):
    '''
    (list,list) -> dictionary
    '''

    temp_dict = {}
    counter = 0
    
    for item in days:
        temp_dict[item] = temps[counter]
        counter += 1

    return temp_dict

dd = createTempD(['Mo', 'Tu', 'We', 'Th', 'Fr','Sa', 'Sun'], [55, 23, 42, 44, 32, 60, 70])

        
def sortTempD(week_dictionary):

    sort_list = []
    for temp in week_dictionary.values():
        sort_list.append(temp)
    sort_list.sort()
    
    return sort_list

def count(alist,item_inalist):
    counter = 0

    for item in alist:
        if item == item_inalist:
            counter += 1

    return counter

def my_in(li,i):
    '''
    (list, int) -> Boolean
    '''

    for item in li:
        if item == i:
            return True

    return False

def my_in_index(li,i):
    '''
    (list, int) -> (Boolean, int)
    '''
    
    for item in li:
        
        if item == i:
            return True
        else:
            counter += 1

    return False, 
        
    
