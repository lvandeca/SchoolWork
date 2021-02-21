#include "stringlist.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define UNUSED __attribute__((unused))

int main(UNUSED int argc, UNUSED char **argv){
	int exitStatus = EXIT_FAILURE;

	const StringList *sl = StringList_create(0L);
	if(sl == NULL){
		fprintf(stderr, "Unable to create StringList to hold input lines");
		goto cleanup;
	}

	char buf[BUFSIZ];
	while(fgets(buf, BUFSIZ, stdin) != NULL){
		char *tmp = strdup(buf);
		int status = sl->append(sl, tmp);
		if(!status){
			fprintf(stderr, "Unable to append line to StringList: %s\n", tmp);
			goto cleanup;	
		}
	}

	long N = sl->size(sl);
	long i;
	for(i = (N-1); i >= 0L; i--) {
		char *sptr[BUFSIZ];
		int success;
		success = sl->get(sl, i, sptr);
		if (success) {
			printf("%s",*sptr);
		} else {
			fprintf(stderr, "Unable to retrieve line %ld\n", i);
			goto cleanup;
		}
	}
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(sl != NULL)
		sl->destroy(sl);
	return exitStatus;
}
