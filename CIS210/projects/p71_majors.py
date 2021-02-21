'''
CIS 210: Majors Data Analysis

Author: Luke Vandecasteele

Credits: Class notes

This function takes an input file and
does a basic data analysis to create a
frequency table as well as return the mode
of the data, and the number of different
items represented.
'''
import doctest

def majors_readf(fname):
    '''
    (string) -> list

    This function takes a file string (fname)
    reads the file, and then converts the items
    in the file in to a list

    >>> majors_readf('1.txt')
    ['PHYS', 'PSY', 'CIS', 'PBA', 'CIS', 'JMS', 'BI', 'BI']
    '''
    
    file_list = []
    empty_string = ''

    item_counter = 0
    counter = 0

    with open(fname) as file:
        new_file = file.read()

    for item in new_file:
        empty_string += item

    for item in empty_string:
        item_counter += 1
        if item == '\n':
            piece = empty_string[counter:item_counter-1]
            counter = item_counter
            file_list.append(piece)
    del file_list[0:2]

    return file_list

def majors_analysis(majorsli):
    '''
    (list) -> tuple

    This function finds the max number
    of an item in the list (majorsli), then writes
    it as a list in a tuple, then writes
    the number of times the item occurs
    in the list (majorsli) also in the tuple.

    >>> majors_analysis(['PHYS', 'PSY', 'CIS', 'PBA', 'CIS', 'JMS', 'BI', 'BI'])
    (['CIS', 'BI'], 2)
    '''
    countdict = {}
    max_tuple = []
    max_list = []
    
    for item in majorsli:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1

    countlist = countdict.values()
    maxcount = max(countlist)

    for item in countdict:
        if countdict[item] == maxcount:
            max_list.append(item)
            
    max_tuple.append(max_list)
    max_tuple.append(maxcount)
    new_max_tuple = tuple(max_tuple)
    
    return new_max_tuple

def majors_report(majors_mode, majors_ct, majorsli):
    '''
    (list,int,list) -> None

    This function gives the number of
    different items represented in a list
    (majorsli), the most represented majors
    (majors_mode), and a frequency table
    for each of the items in (majorslie)

    >>> majors_report(['CIS', 'EXPL'], 3, ['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    3 majors are represented in CIS 210 this term
    The most represented major(s) are: CIS EXPL
    Item Frequency
    CIS     2
    COLT    1
    EXPL    2
    '''
    countdict = {}
    
    for item in majorsli:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1
        
    print(len(countdict), 'majors are represented in CIS 210 this term')

    rep_majors = ' '.join(majors_mode)
    print('The most represented major(s) are:', rep_majors)

    itemlist = list(countdict.keys())
    itemlist.sort()

    print('Item','Frequency')

    for item in itemlist:
        if len(item) == 3:
            print(item, '    ', countdict[item])
        elif len(item) == 2:
            print(item, '     ', countdict[item])
        else:
            print(item, '   ', countdict[item])
        
    return None

def main():
    '''()-> None

    Calls: majors_readf, majors_analysis, majors_report

    Top level function for analysis of CIS 210 majors data. '''

    #fname = 'p71-majors-short.txt'
    fname = 'p71-majors.txt'

    majorsli = majors_readf(fname) #read
    majors_mode, majors_ct = majors_analysis(majorsli) #analyze
    majors_report(majors_mode, majors_ct, majorsli) #report
    return None

main()


    
