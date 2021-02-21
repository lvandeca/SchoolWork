'''
More Automated Testing and Debugging
CIS 210 Project 6-2 Winter 2020

Functions need to be tested and debugged;
write a function to automate testing of calendar function (project 5-1)

Author: Luke Vandecasteele

Credits: Class notes
'''
import doctest

def bigSalesBug(sales_list):
    '''(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40000, 45.67, 19000.0, 25000, 100000])
    140000.0

    >>> bigSalesBug([])
    0.0

    >>> bigSalesBug([0])
    0.0
    '''
    total = 0.0
    for item in sales_list:     #syntax error
        if item >= 40000:        #syntax error and > was changed to >=
            total = total + item
    return total

############

def findRangeBug(salesli):
    '''(list) -> tuple

    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)

    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)

    >>> findRangeBug([0])
    (0.0, 0.0)

    >>> findRangeBug([1,1,1,3])
    (1.0, 3.0)
    '''
    salesli.sort()      #changed to just salesli.sort() rather than setting equal to a variable because sort function returns none
    len_salesli = len(salesli) - 1 
    l = float(salesli[0])
    h = float(salesli[len_salesli]) #changed to length of the list because -1 doesn't work
    return l, h

def salesReportBug(salesli):
    '''(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    >>> salesReportBug([40000, 45.67, 19000.0, 25000, 100000])
    Weekly Range: $45.67 - $100,000.00
    Mon          Tue          Wed          Thu          Fri         
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00
    '''
    og_salesli = salesli.copy() #made a copy of the original list so that it isn't sorted when we print the amount of money each day
    #calculate and report low and high sales
    low, high = findRangeBug(salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}')
    #print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    #report on sales per day from list data
    for sales in og_salesli:
        print(f'${float(sales):<{fw},.2f}', end='')
        
    return None

print(doctest.testmod())
