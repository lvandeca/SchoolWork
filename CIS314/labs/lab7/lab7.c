/*
Author: Luke Vandecasteele
Date: 2/23/2021
Description: Practice optimizing code for speed
*/

//function to optimize
/*
void g(int **arr, int *res) {
    *res = 0;
    for (int j = 0; j < numColumns(arr); ++j) {
        for (int i = 0; i < numRows(arr); ++i) {
            *res &= arr[i][0] + arr[i][j];
        }
    }
}
*/

//optimized version
void g(int **arr, int *res)
{
    int result = 0;
    int rows = numRows(arr);
    int columns = numColumns(arr);

    for (int i = 0; i < rows; ++i)
    {
        int *row = &arr[i];
        int rowVal = *row;

        for (int j = 0; j < columns; ++j)
        {
            result &= rowVal + *row++;
        }
    }

    *res = result
}