#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *integerArray = (int *)malloc(sizeof(int *) * 4);

    int i;
    for (i = 0; i < 4; i++)
    {
        integerArray[i] = i + 1;
    }

    for (i = 0; i < 4; i++)
    {
        int tmp = integerArray[i];
        printf("%d\n", tmp);
    }

    free(integerArray);
}
