'''
CIS 210: Earthquake Data

Author: Luke Vandecasteele

Credits: Class notes

This function finds the magnitude of
earthquakes from a set of data and then analyzes
the data to give the mode, median, and mean
of the data.
'''
def equake_readf(fname):
    '''
    (string) -> list

    This function takes a string file (fname)
    and returns the data in the file as a list
    '''

    with open(fname) as file:
        the_file = file.read()

    equake_file = the_file.readline().strip().split('\n')

    print(equake_file)
    return None
