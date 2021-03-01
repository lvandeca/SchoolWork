/*
Author: Luke Vandecasteele
Date: 2/28/2021 Last Modified: 2/28/2021
Credits: Class notes and powerpoints
Description: Optimizing code by limiting operations within for loops
*/

#include <stdio.h>

/*
// code to be fixed. move non-dependant multiplications outside the loops
intf(int a, int b, int c, int d, int n)
{
    int result = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            result += a * b + i * c * d + j;
        }
    }
    return result;
}
*/

int f(int a, int b, int c, int d, int n)
{
    int result = 0;
    int ab = a * b; //move a*b and c*d operations outside
    int cd = c * d; //can only move these two to preserve
                    //order of operations of the function
    for (int i = 0; i < n; ++i)
    {
        int abicd = ab + i * cd; //don't need to do this every single
                                 //inside the inner for loop
        for (int j = 0; j < n; ++j)
        {
            result += abicd + j;
        }
    }
    return result;
}

int main()
{

    //test functions for our progra

    printf("f(1, 2, 3, 4, 5): 700, Actual: %d\n", f(1, 2, 3, 4, 5));
    printf("f(2, 3, 4, 5, 6): 2106, Actual: %d\n", f(2, 3, 4, 5, 6));
    printf("f(6, 5, 4, 3, 2): 146, Actual: %d\n", f(6, 5, 4, 3, 2));
    printf("f(5, 4, 3, 2, 1): 20, Actual: %d\n", f(5, 4, 3, 2, 1));
}