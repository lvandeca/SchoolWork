'''
CIS 210: Inspecting Files

Author: Luke Vandecasteele

Credits: class notes and Morgan Freeman

This project calls a file and returns the number of lines
characters in the file along with a frequency chart of the
different types of words in the file
'''
import doctest

def fcounts(fname):
    '''
    (string) -> None

    This funtion opens a file
    (fname) and counts the number of characters
    and lines in the file as well as generates
    a frequency table of the different words in
    the file

    >>> fcounts('p74_text.txt')
    The number of lines in file p74_text.txt is: 8
    The number of characters in file p74_text.txt is: 51
    Item            Frequency
    all             1
    greatest             1
    is             1
    luke             1
    of             1
    player             1
    tennis             1
    the             1
    time             1
    vandecasteele             1
    '''
    
    with open(fname) as file:
        the_file = file.read()

    line_counter = 0
    char_counter = 0
    space_counter = 0
    countdict = {}

    for item in the_file:
        if item == '\n' :
            line_counter += 1
        elif item == ' ':
            space_counter += 1
        else:
            char_counter += 1

    print('The number of lines in file', fname, 'is:', line_counter)
    print('The number of characters in file', fname, 'is:', char_counter)

    empty_string = ''
    empty_list = []
    countdict = {}
    total = 0
    word_total = 0

    for item in the_file:
        empty_string += item
    
    for item in the_file:
        total += 1
        if item == ' ' or item == '\n':
            piece = empty_string[word_total:total-1]
            empty_list.append(piece)
            word_total = total
    
    for item in empty_list:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1
            
    itemlist = list(countdict.keys())
    itemlist.sort()

    print('Item','          ', 'Frequency')

    for item in itemlist:
        print(item, '           ', countdict[item])
    
    return None

def main():
    '''
    Main program driver funtion
    '''
    
    fcounts('p74_text.txt')
    return None

main()
