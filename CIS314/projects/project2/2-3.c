#include <stdio.h>

int le(float x, float y) {
	unsigned int ux = *((unsigned int *) &x); //convert x raw bits
	unsigned int uy = *((unsigned int *) &y); //convert y raw bits

	unsigned int sx = ux >> 31; //extract sign bit of ux
	unsigned int sy = uy >> 31; //extract sign bit of uy

	ux <<= 1; //drop sign bit of ux
	uy <<= 1; //drop sign bit of uy

	// my return status is here:
	int status = 	(ux == 0 && uy == 0) | 				// 1 if x = +-0.0 and y = +-0.0
			(sx == 1 && sy == 0) |				// 1 if x is negative and y is positive
			((sx == 1 && sy == 1) & (ux >= uy)) |		// 1 if x and y are negative, and ux >= uy
			((sx == 0 && sy == 0) & (ux <= uy));		// 1 if x and y are positive, and ux <= uy
	
	return status;
}

int main() {

	printf("le(0.0f, 0.0f): %d\n", le(0.0f, 0.0f));
	printf("le(-0.0f, 0.0f): %d\n", le(-0.0f, 0.0f));
	printf("le(-1.0f, -1.0f): %d\n", le(-1.0f, 0-1.0f));

	printf("le(1.0f, 1.0f): %d\n", le(1.0f, 1.0f));
	printf("le(-1.0f, 0.0f): %d\n", le(-1.0f, 0.0f));
	printf("le(0.0f, 1.0f): %d\n", le(0.0f, 1.0f));

	printf("le(1.0f, 0.0f): %d\n", le(1.0f, 0.0f));
	printf("le(0.0f, -1.0f): %d\n", le(0.0f, -1.0f));
	printf("le(-1.0f, -2.0f): %d\n", le(-1.0f, -2.0f));

	return 1;
}
