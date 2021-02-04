#include <stdio.h>

unsigned int extract(unsigned int x, int i) {
	/* The first step is to shift x left (3 - i) bytes
	 * removing the bits to the left of our target 
	 * byte, i. The second step is to arthmetic shift 
	 * all the way left, removing all the bits to the 
	 * right we don't want, and simultaneously sign 
	 * extending our returned integer.
	 * */

	int remove = x << ((3 - i) << 3);	
	return remove >> 24;		
}					


int main() {
	printf("extract(0x12345678, 0): %x\n", extract(0x12345678, 0));
	printf("extract(0xabcdef00, 2): %x\n", extract(0xabcdef00, 2));
	
	return 1;
}
