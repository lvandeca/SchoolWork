#include <stdio.h>

/*problem 1:
  00010111
  00111011 &
  --------
  00010011
*/


//problem 2:
int isNegativeOrZero(int x){
	int neg = x & 0x80000000;
	int zero = !x;
	return neg || zero;
}

void main() {
	printf("Test -45: %i\n", isNegativeOrZero(-45));
	printf("Test 0: %i\n", isNegativeOrZero(0));
	printf("Test 14: %i\n", isNegativeOrZero(14));
}
