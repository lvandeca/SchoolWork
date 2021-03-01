/*
Author: Luke Vandecasteele
Date: 2/28/2021 Last Modified: 2/28/2021
Credits: Class notes and powerpoints
Description: Practicing using loop unrolling for optimization
*/

#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>

void inner(float *u, float *v, int length, float *dest)
{
    int i;
    float sum = 0.0f;
    for (i = 0; i < length; ++i)
    {
        sum += u[i] * v[i];
    }
    *dest = sum;
}

void inner2(float *u, float *v, int length, float *dest)
{
    int i;
    float sum = 0.0f;
    int limit = length - 3;

    float x0, x1, x2, x3;
    x0 = x1 = x2 = x3 = 0.0f;

    // Combine 4 elements from each array at a time
    for (i = 0; i < limit; i += 4)
    {
        x0 += u[i] * v[i];
        x1 += u[i + 1] * v[i + 1];
        x2 += u[i + 2] * v[i + 2];
        x3 += u[i + 3] * v[i + 3];
    }

    for (; i < length; i++)
    {
        x0 += u[i] * v[i];
    }

    *dest = x0 + x1 + x2 + x3;
}

int main()
{
    //general purpose testing to make sure that our loop unrolling is correct
    //as well as to generate date for our graph in part (d) of the question

    float dest = 0.0f;
    float dest2 = 0.0f;
    clock_t start;
    clock_t end;
    double seconds;

    int i;

    printf("===============================test 1========================================\n");
    float u[100];
    float v[100];

    for (i = 0; i < 100; i++)
    {
        u[i] = i;
        v[i] = i;
    }

    //inner
    start = clock();
    inner(u, v, 100, &dest);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);

    //inner2
    start = clock();
    inner2(u, v, 100, &dest2);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);

    printf("===============================test 2========================================\n");
    float u1[10000];
    float v1[10000];

    for (i = 0; i < 10000; i++)
    {
        u1[i] = i;
        v1[i] = i;
    }

    //inner
    start = clock();
    inner(u1, v1, 10000, &dest);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);

    //inner2
    start = clock();
    inner2(u1, v1, 10000, &dest2);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);

    printf("===============================test 3========================================\n");
    float u2[1000000];
    float v2[1000000];

    for (i = 0; i < 1000000; i++)
    {
        u2[i] = i;
        v2[i] = i;
    }

    //inner
    start = clock();
    inner(u2, v2, 1000000, &dest);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);

    //inner2
    start = clock();
    inner2(u2, v2, 1000000, &dest2);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);
}