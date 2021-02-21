'''                          # FILE HEADER
Nature's Thermometer: Cricket Chirps.
CIS 210 W20 Project 1-1 Hello-Cricket

Author: Luke Vandecasteele

Credits: class text notes

Determine the temperature based on cricket
chirps. (Farmers Almanac)
'''

breakpoint()

def chirps_to_ctemp(n):  #FUNCTION HEADER
    '''(int) -> float       #TYPE CONTRACT
                            #BRIEF DESCRIPTION refers to
                            #PARMS, RETURN VAL
    Return celsius temp estimated based on
    number of cricket chirps in a 25 second
    interval (ch25) - divide by 3 and add 4
    to get the celsius temperature.
                            #EXAMPLES OF USE
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''
    #replace pass with your code - don't forget to include return
    ctemp = (n/3 + 4)
    return ctemp

def chirps_to_ftemp(x):
    '''(int) -> int #type contract

    Return fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40.  The estimated
    temperature is returned. #description

    >>> chirps_to_ftemp(0)
    40
    >>> chirps_to_ftemp(50)
    90
    #examples
    '''    
    #replace pass with your code - don't forget to include return
    ftemp = 40 + x
    return ftemp

