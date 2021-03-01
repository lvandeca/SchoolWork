/*
Author: Luke Vandecasteele
Date: 2/28/2021 Last Modified: 2/28/2021
Credits: Class notes and powerpoints
Description: Analyzing if statements within loops
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

float f(float *a, int n)
{
    float prod = 1.0f;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] != 0.0f)
        {
            prod *= a[i];
        }
    }
    return prod;
}

float g(float *a, int n)
// same as function f() without the if statement
{
    float prod = 1.0f;
    for (int i = 0; i < n; ++i)
    {
        prod *= a[i];
    }
    return prod;
}

float *createArray(int size)
{
    float *a = (float *)malloc(size * sizeof(float));
    for (int i = 0; i < size; ++i)
    { // 50% chance that a[i] is 0.0f, random value on the range
        // [0.76, 1.26] otherwise.
        float r = rand() / (float)RAND_MAX;
        a[i] = r < 0.5f ? 0.0f : r + 0.26f;
    }
    return a;
}

int main()
{
    //====================================part (a)=============================
    float *a;
    a = createArray(1000);

    clock_t start = clock();
    float product = f(a, 1000);
    clock_t end = clock();

    double seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    //print time for a aka f(a)
    printf("time for a: %f\n", seconds);
    //print the results of f() to avoid deade code removal
    printf("%f\n", product);
    free(a);

    //====================================part (b)=============================

    float *b = (float *)malloc(1000 * sizeof(float));
    for (int i = 0; i < 1000; i++)
    {
        if (b[i] == 0.0f)
        {
            b[i] = 1.0f;
        }
    }

    start = clock();
    product = g(b, 1000);
    end = clock();
    free(b);

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    //print time for c aka g(b)
    printf("time for b: %f\n", seconds);
    //print the results of g() to avoid dead code removal
    printf("%f\n", product);

    /*
    The time to run function g() is about half the time to run function f()
    (i.e. function g() is much faster). This is because by removing the if 
    statement within the for loop we are removing the 50% chance that our 
    computer is predicting just in case we enter the if statement. 
    */

    //====================================part (c)=============================

    float *c = (float *)malloc(1000 * sizeof(float));
    for (int i = 0; i < 1000; i++)
    {
        if (a[i] != 0.0f)
        {
            c[i] = a[i];
        }
    }

    start = clock();
    product = g(c, sizeof(c));
    end = clock();
    free(c);

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    //print time for c, aka g(c)
    printf("time for c: %f\n", seconds);
    //print the results of g() to avoid dead code removal
    printf("%f\n", product);

    /*
    Again, running g(c) is much faster than f(a) or g(b). The reason for this 
    is similar to the last question in that we are no longer forcing our 
    computer and compiler to guess about the values in our table. We know that
    we enter our for loop every single time other than the last, so if our 
    computer guesses that we will enter the for loop and does that
    calculation ahead of time, then it will only be wrong one time (i.e the 
    last time throught the loop). Therefore our code gets much faster because
    our computer will only guess wrong one time.
    */
}