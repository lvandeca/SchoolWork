#include <stdio.h>

unsigned int combine(unsigned int x, unsigned int y) {
	unsigned int firstBits = 0xFF & y;			//mask the first byte from y with an and
	unsigned int lastBits = 0xFFFFFF00 & x;			//mask bytes 1 through 3 from x with an and
	unsigned int combined = lastBits | firstBits;		//combine the bytes from both with inclusive or

	return combined;
}

void main() {
	printf("Testing 0x12345600: %x\n", combine(0x12345678, 0xABCDEF00));
	printf("Testing 0xABCDEF78: %x\n", combine(0xABCDEF00, 0x12345678));
}
