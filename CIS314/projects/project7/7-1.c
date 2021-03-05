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
    return (address >> 8) & 0xF; //shift to get rid of offset bits and then git 4 bits
}

unsigned int getTag(unsigned int address)
{
    return address >> 12; //shift to remove bottom 12 bits and then get remaining for tag
}

int main()
{
    printf("0x12345678\n");
    printf("Offset: %x - Tag: %x - Set: %x\n", getOffset(0x12345678),
           getTag(0x12345678), getSet(0x12345678));
    printf("0x87654321\n");
    printf("Offset: %x - Tag: %x - Set: %x\n", getOffset(0x87654321),
           getTag(0x87654321), getSet(0x87654321));
}