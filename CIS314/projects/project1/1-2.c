#include <stdio.h>

unsigned int replace(unsigned int x, int i, unsigned char b) {
	//first, shift mask over to correct byte, then and those bits from x
	//second, remove that byte from x so that byte is now empty
	unsigned int removed = x - (x & (0xFF << (i * 8)));

	//shift over input byte to correct byte location
	unsigned int shifted = b << (i * 8);
	unsigned int replaced = removed | shifted;	//combine x with the cleared byte location, with the inpute byte using an or

	return replaced;
}

void main() {
	printf("Test 0xab345678: %x\n", replace(0x12345678, 3, 0xab));
	printf("Test 0x123456ab: %x\n", replace(0x12345678, 0, 0xab));
}

