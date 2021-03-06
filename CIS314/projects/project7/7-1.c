/*
Author: Luke Vandecasteele
Date: 3/3/2021 Last Modified: 3/4/2021
Credits: Class notes and powerpoint
Description: Breaking down bits of an address using bitwise operations
*/

#include <stdio.h>

unsigned int getOffset(unsigned int address)
{
    return address & 0xFF; //get bottom 8 bits
}

unsigned int getSet(unsigned int address)
{
    return (address >> 8) & 0xF; //shift to get rid of offset bits and then get 4 bits
}

unsigned int getTag(unsigned int address)
{
    return address >> 12; //shift to remove bottom 12 bits and then get
                          //remaining bits for tag
}

int main()
{
    //couple of test cases for our address calculator
    printf("=================Test case 1==================\n");
    printf("0x12345678: ");
    printf("Offset: %x - Tag: %x - Set: %x\n", getOffset(0x12345678),
           getTag(0x12345678), getSet(0x12345678));

    printf("=================Test case 2==================\n");
    printf("0x87654321: ");
    printf("Offset: %x - Tag: %x - Set: %x\n", getOffset(0x87654321),
           getTag(0x87654321), getSet(0x87654321));
}