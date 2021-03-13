#include <stdio.h>

int main()
{
    int *array = (int *)malloc(sizeof(int) * 16);

    for (int i = 0; i < 16; i++)
    {
        array[i] = i;
    }

    for (int j = 0; j < 16; j++)
    {
        printf("%c\n", array[j])
    }
}