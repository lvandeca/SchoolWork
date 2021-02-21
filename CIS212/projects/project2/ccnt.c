#include <stdio.h>
#include <stdlib.h>
#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char *argv[]){
	long nchars = 0L;
	char buf[BUFSIZ];
	int exitStatus = EXIT_SUCCESS;
	char* p = NULL;

	while (fgets(buf, sizeof buf, stdin) != NULL){
		for (p = &buf[0]; *p != '\0'; p++){
			nchars++;	
		}
	}
	printf("%8ld\n", nchars);
	return exitStatus;
}
