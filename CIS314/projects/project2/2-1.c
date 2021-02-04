#include <stdio.h>

unsigned int mask(int n) {
	/*First we create a full 32 bit mask. Next,
	 * we shift left n bits to the bits we don't
	 * wantin out new mask. Finally, this
	 * shifted number is subtracted from our 
	 * full mask, creating a mask with only the
	 * desired n bits. */

	unsigned int full = 0xffffffff;		
	return full - (full << n);		
}						
							

int  main() {					
	printf("mask(1): %x\n", mask(1));
	printf("mask(2): %x\n", mask(2));
	printf("mask(3): %x\n", mask(3));
	printf("mask(5): %x\n", mask(5));
	printf("mask(8): %x\n", mask(8));
	printf("mask(16): %x\n", mask(16));
	printf("mask(31): %x\n", mask(31));

	return 1;
}

