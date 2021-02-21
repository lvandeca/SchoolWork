#include <stdio.h>
#include <stdlib.h>
#define UNUSED __attribute__((unused))
#include "stsplit.h"

void countLWC(FILE *fd, long *nl, long *nw, long *nc){
	char buf[BUFSIZ];
	char *p = NULL;
	int i;

	while (fgets(buf, sizeof buf, fd) != NULL){
		(*nl)++;
		char **words = stsplit(buf);
		for(i = 0; words[i] != NULL; i++){
			(*nw)++;
		}
		for(p = &buf[0]; *p != '\0'; p++){
			(*nc)++;
		}
		stfree(words);
	}
}

int main(UNUSED int argc, UNUSED char *argv[]){
	long nlines = 0L;
	long nwords = 0L;
	long nchars = 0L;

	int exitStatus = EXIT_SUCCESS;

	countLWC(stdin, &nlines, &nwords, &nchars);
	
	printf("%8ld %8ld %8ld\n", nlines, nwords, nchars);
	return exitStatus;
}
