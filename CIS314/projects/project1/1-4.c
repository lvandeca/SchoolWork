#include <stdio.h>

void printBytes(unsigned char *start, int len) {
	for (int i = 0; i < len; i ++) {
		printf("%.2x", start[i]);
	}
	printf("\n");
}

void printInt(int x){
	printBytes((unsigned char *) &x, sizeof(int));
}

void printFloat(float x){
	printBytes((unsigned char *) &x, sizeof(float));
}

void printShort(short x){
	printBytes((unsigned char *) &x, sizeof(float));
}

void printLong(long x){
	printBytes((unsigned char *) &x, sizeof(long));
}

void printLongLong(long long x){
	printBytes((unsigned char *) &x, sizeof(long long));
}

void printDouble(double x){
	printBytes((unsigned char *) &x, sizeof(double));
}

/*Some things I noticed using these functions:
 * 1) 	The digits printed on the output each time are in hexadecimal
 * 2) 	Depending on the data type, the representative amount of bytes are
 * 		printed i.e. printInt() will print out 32 bits in 
 * 		hexadecimal
 * 3) 	Long and Long Long have the same number of bytes being represented
 * 		even though they are different data types. Upon further 
 * 		investigation, a Long Long simply guarantees that 64 bits
 * 		will be used in memory, whereas a Long changes depending
 * 		upon the input
 * 4)	Since we used unsigned integers for the other programs we wrote, it
 * 		is interesting how the range changes drastically using an 
 * 		int rather than the unsigned version.
 * 5)	We haven't talked much about floats yet, but the representation is 
 * 		rather confusing so far, and as such I'm not exactly sure 
 * 		what the hexadecimal representation is showing. Same for
 * 		doubles.
 */


void main() {
	printf("Integer 23423: ");
	printInt(23423);

	printf("Float 234.234: ");
	printFloat(234.234);

	printf("Short 534:");
	printShort(534);

	printf("Long 4374768438: ");
	printLong(4374768435768);

	printf("Long Long 547685467857854: ");
	printLong(547685467857854);

	printf("Double 33453.23455: ");
	printDouble(33453.23455);

}
