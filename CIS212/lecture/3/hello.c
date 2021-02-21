#include <stdio.h> /* gives us access to functions for input/output */
#include <stdlib.h> /* gives us us access to EXIT_SUCCESS */

#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]) { /*we have to define main */
	printf("Hello World!\n"); /*print "Hellow World!" on standard output */
	return EXIT_SUCCESS;	  /* indicates successfull execution */
}

