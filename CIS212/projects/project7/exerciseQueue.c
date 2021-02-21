#include "ADTs/llistqueue.h"
#include "ADTs/queue.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void freeValue(void *v){
	if(v != NULL)
		free(v);
}

void printQueue(const Queue *q, FILE *fd) {
	long value;
	int first = 1;
	const Iterator *it = NULL;

	if(q->isEmpty(q)) {
		fprintf(fd, "Empty\n");
		return;
	}

	it = q->itCreate(q);
	if(it != NULL) {
		while(it->hasNext(it)) {
			(void) it->next(it, (void **)&value);
			char *prefix = (first) ? "" : " ";
			first = 0;
			fprintf(fd, "%s%ld", prefix, value);
		}
		it->destroy(it);
	}
	
	fprintf(fd, "\n");
}

void exerciseQueue(FILE *fd, const Queue *q) {
	char buf[BUFSIZ];
	int N, i;

	(void)fgets(buf, BUFSIZ, fd);
	(void)sscanf(buf, "%d", &N);

	for(i = 0; i < N; i++) {
		(void)fgets(buf, BUFSIZ, fd);
		if(strcmp(buf, "dequeue\n") == 0) {
			long v;
			if(!q->dequeue(q, (void **)&v)) {
				printf("QueueError\n");
			} else {
				printf("%ld\n", v);
			}
		} else if(strcmp(buf, "print\n") == 0) {
			printQueue(q, stdout);
		} else {
			long v;
			sscanf(buf+8, "%ld", &v);
			(void) q->enqueue(q, (void *)v);
		}
	}
}

int main(int argc, char *argv[]) {
	FILE *fd = NULL;
	const Queue *q = NULL;
	int exitStatus = EXIT_FAILURE;

	if(argc != 2) {
		fprintf(stderr, "usage: %s file\n", argv[0]);
		goto cleanup;
	}

	if((fd = fopen(argv[1], "r")) == NULL) {
		fprintf(stderr, "%s: cannot open file %s\n", argv[0], argv[1]);
		goto cleanup;
	}

	if((q = Queue_create(freeValue)) == NULL) {
		fprintf(stderr, "%s: cannot create Queue ADT instance\n", argv[0]);
		goto cleanup;
	}

	exerciseQueue(fd, q);
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(q != NULL)
		q->destroy(q);
	if(fd != NULL)
		fclose(fd);
	return exitStatus;
}
