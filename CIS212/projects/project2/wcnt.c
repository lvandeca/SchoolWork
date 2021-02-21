#include <stdio.h>
#include <stdlib.h>
#define UNUSED __attribute__((unused))
#include "stsplit.h"

int main(UNUSED int argc, UNUSED char *argv[]){
	long nchar = 0L;
	char buf[BUFSIZ];
	int exitStatus = EXIT_SUCCESS;
	int i;

	while (fgets(buf, sizeof buf, stdin) != NULL) {
		char **words = stsplit(buf);
	for(i = 0; words[i] != NULL; i++){
		nchar++;
	}
	stfree(words);
	}
	printf("%8ld\n", nchar);
	return exitStatus;
}
