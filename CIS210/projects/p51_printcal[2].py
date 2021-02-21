'''
CIS 210 Calendar Function

Author: Luke Vandecasteele

Credits: Class notes, Isais,python.com

This fuction prints the calendar for a given month and year,
or prints the entire year if there is no input.

'''

import datetime
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

def calendar(month, year):
    '''
    (int, int) -> None

    Prints a calendar for
    given month and year.
    
    '''
    if is_leap(year):
        days_in_month[1] = 29
    month_corrected = month_list[month-1]
    num_days = days_in_month[month-1]
    day_one = datetime.date(year, month, 1)
    start_day = day_one.isoweekday()
    
    print(month_corrected[:3], year)
    print(' '.join(['{0:<2}'.format(w) for w in days_of_week]))
    print('{0:>3}'.format('')*start_day, end='')

    if start_day >= 7:
        print()
        start_day = 0
    
    for day in range(1, num_days+1):
        print('{0:>2}'.format(day), end=' ')
        start_day += 1
        if start_day >= 7:
            print()
            start_day = 0
    print()

def is_leap(year):
    '''
    (int) -> bool

    Checks if year is a leap year
    credit to Steven Summers

    CALLS:

    CALLED BY: calendar()

    >>> is_leap(2000)
    True
    >>> is_leap(1900)
    False
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    '''
    () -> None

    Drives calendar program

    Examples:
    '''
    for i in range(1,13):
        calendar(i, 2020)
        main()

if __name__ == '__main__':
    main()
