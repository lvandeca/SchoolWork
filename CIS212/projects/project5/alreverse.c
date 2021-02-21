#include "ADTs/arraylist.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char **argv){
	int exitStatus = EXIT_FAILURE;

	const ArrayList *al = ArrayList_create(0L, free);
	if(al == NULL){
		fprintf(stderr, "Unable to create ArrayList to hold input line\n");
		goto cleanup;
	}

	char buf[BUFSIZ];
	while(fgets(buf, BUFSIZ, stdin) != NULL){
		char *tmp = strdup(buf);
		int status = al->add(al, tmp);
		if(!status){
			fprintf(stderr, "Unable to append line to ArrayList: %s\n", tmp);
			goto cleanup;	
		}
	}

	long N = al->size(al);
	long i;
	for(i = (N-1); i >= 0L; i--) {
		char *sptr;
		int success;
		success = al->get(al, i, (void**)&sptr);
		if (success){
			printf("%s", sptr);
		} else {
			fprintf(stderr, "Unable to retrieve line %ld\n", i);
			goto cleanup;
		}
	}
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(al != NULL)
		al->destroy(al);
	return exitStatus;
}
