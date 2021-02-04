#include <stdio.h>

int oddBit(unsigned int x){
	int isOdd = 0;
	unsigned int mask = 0xaaaaaaaa;		//mask with bits only in the odd positions
	if(mask & x) {				//by &ing our mask with x, if there are bits in the
		isOdd = 1;			//odd position, we will get an int other than 0, so the if statement is true
	}
	return isOdd;
}

void main() {
	printf("Test 0: %d\n", oddBit(0x1));
	printf("Test 1: %d\n", oddBit(0x2));
	printf("Test 1: %d\n", oddBit(0x3));
	printf("Test 0: %d\n", oddBit(0x4));
	printf("Test 1: %d\n", oddBit(0xffffffff));
	printf("Test 1: %d\n", oddBit(0xaaaaaaaa));
	printf("Test 0: %d\n", oddBit(0x55555555));
}
