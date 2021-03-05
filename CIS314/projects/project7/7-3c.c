/*
Author: Luke Vandecasteele
Date: 3/3/2021 Last Modified: 3/4/2021
Credits: Class
notes and powerpoints
Description: Optimizing code by analyzing memory lookups and limiting memory
             access by ensuring that larger blocks are available in our cache 
             for accessing.
*/
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

struct ColorPoint
{
    long a;
    long r;
    long g;
    long b;
};

long f(struct ColorPoint **points, int n)
{
    long sum = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            sum += points[j][i].a;
            sum += points[j][i].r;
            sum += points[j][i].g;
            sum += points[j][i].b;
        }
    }
    return sum;
}

long g(struct ColorPoint **points, int n)
{
    long sum = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            sum += points[i][j].a;
            sum += points[i][j].r;
            sum += points[i][j].g;
            sum += points[i][j].b;
        }
    }
    return sum;
}

struct ColorPoint **create2DArray(int n)
{
    // Array to hold a pointer to the beginning of each row
    struct ColorPoint **points =
        (struct ColorPoint **)malloc(n * sizeof(struct ColorPoint *));
    for (int i = 0; i < n; ++i)
    {
        // Array to hold each row
        points[i] =
            (struct ColorPoint *)malloc(n * sizeof(struct ColorPoint));
        for (int j = 0; j < n; ++j)
        {
            // Init the ColorPoint struct
            points[i][j].a = rand();
            points[i][j].r = rand();
            points[i][j].g = rand();
            points[i][j].b = rand();
        }
    }
    return points;
}
void free2DArray(struct ColorPoint **points, int n)
{
    for (int i = 0; i < n; ++i)
    {
        free(points[i]);
    }
    free(points);
}

int main()
{
    struct ColorPoint **points = create2DArray(2048);
    clock_t start;
    clock_t end;
    double seconds;

    //test time for f()
    start = clock();
    int sum = f(points, 2048);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("f() sum: %d ", sum);
    printf("time f(): %f\n", seconds);

    //test time for g()
    start = clock();
    sum = g(points, 2048);
    end = clock();

    seconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("f() sum: %d ", sum);
    printf("time g(): %f\n", seconds);

    free2DArray(points, 2048);

    /*
    The reason that functin g() is so much faster is simply because we are
    making less memory access. As we have learned, accessing our cache is much
    faster than going into memory and finding an element. Therefore, since we
    have fewer misses in the cache, then our code accessing memory less, and
    becomes faster!
    */
}
