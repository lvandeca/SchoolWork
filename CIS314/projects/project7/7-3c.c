#include <stdlib.h>
#include <stdio.h>

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
    //Array to hold a pointer to the beginning of each row
    struct ColorPoint **points =
        (struct ColorPoint **)malloc(n * sizeof(struct Colorpoint *));
    for (int i = 0; i < n; ++i)
    {
        //Array to hold each row
        points[i] =
            (struct Colorpoint *)malloc(n * sizeof(struct Colorpoint *));
    }
}