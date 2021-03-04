#include <stdio.h>

unsigned int getOffset(unsigned int address)
{
    return address & 0xFF;
}

unsigned int getSet(unsigned int address)
{
    return (address >> 8) & 0xF;
}

unsigned int getTag(unsigned int address)
{
    return address >> 12;
}

int main()
{
    printf("0x12345678\n");
    printf("Offset: %x - Tag: %x - Set: %x\n", getOffset(0x12345678),
           getSet(0x12345678),
           getTag(0x12345678));
    printf("0x87654321\n");
}