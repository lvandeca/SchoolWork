'''
Determining Net Pay
CIS 210 Project 2-1 Net Pay

Author: Luke Vandecasteele

Credits: Class Notes

Learning to write functions that call other
functions in order to have smaller functions
for better organization
'''

def tax(gross_pay):
    '''
    - (float) -> float
    - This function calculated the taxable
    amount based on gross pay
    - Examples:
    >>> tax(100)
    15.0
    >>> tax(122.5)
    18.375
    >>> 
    '''
    tax_amount = gross_pay * 0.15
    return tax_amount

def netpay(hours_worked):
    '''
    - (int) -> float
    - This function calculates the net pay
    of an employee based on the number of hours
    worked (hours_worked).
    -Examples:
    >>> netpay(1)
    9.56
    >>> netpay(40)
    382.5
    '''
    gross_pay = hours_worked * 11.25
    tax_amount = tax(gross_pay)
    net_pay = gross_pay - tax_amount
    round_net_pay = round(net_pay,2)
    return round_net_pay

def main():
    '''Net pay program driver.'''
    print('For 1 hours work, netpay is: ', netpay(1))
    print('For 40 hours work, netpay is: ', netpay(40))
    return None

main()
