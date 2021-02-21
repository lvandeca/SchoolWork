#include "ADTs/stack.h"
#include <stdlib.h>
#include <stdio.h>
#include "string.h"
#include <stdbool.h>

int isOpen(char bracket) {
	char p = '(';
	char s = '[';
	char c = '{';
	char t = '<';

	if(p == bracket)
		return 1;
	if(s == bracket)
		return 1;
	if(c == bracket)
		return 1;
	if(t == bracket)
		return 1;

	return 0;
}

char getPair(char bracket) {
	char p = '(';
	char s = '[';
	char c = '{';
	char t = '<';

	if(p == bracket)
		return ')';
	if(s == bracket)
		return ']';
	if(c == bracket)
		return '}';
	if(t == bracket)
		return '>';

	return 'N';
}

int main(int argc, char *argv[]) {
	FILE *fd;
	const Stack *st = Stack_create(NULL);
	int exitStatus = EXIT_FAILURE;
	long numlines;
	char buf[BUFSIZ];

	if(argc != 2) {
		fprintf(stderr, "Incorrect usage. Usage: %s file\n", argv[0]);
		goto cleanup;
	}

	if((fd = fopen(argv[1], "r")) == NULL) {
		fprintf(stderr, "Unable to open given file: %s\n", argv[1]);
		goto cleanup;
	}

	if(st == NULL) {
		fprintf(stderr, "Cannot create stackADT...\n");
		goto cleanup;
	}

	fgets(buf, BUFSIZ, fd);
	sscanf(buf, "%ld", &numlines);
	while(numlines-- > 0) {
		fgets(buf, BUFSIZ, fd);
		int i = 0;
		while(buf[i] != '\n') {
			char c = buf[i];

			//if the stack is empty, push the the first element onto the stack
			if(st->isEmpty(st)){
				(void) st->push(st, (void *)(long)c);

			//if next element is an open bracket, push it onto the stack
			} else if(isOpen(c)) {
				(void) st->push(st, (void *)(long)c);

			//next element is not open
			} else {
				long peek;
				(void) st->peek(st, (void **)&peek);
				char matchPeek = getPair((char)peek);

				//if element is a match for previous element (i.e. the peeked element in stack)
				//then pop previous element in stack
				if(buf[i] == matchPeek) {
					long remove;
					(void) st->pop(st, (void**)&remove);

				//if not, then not balanced, break
				} else {
					break;
				}	
			}
			i++;
		}
		if(st->isEmpty(st)) {
			printf("YES\n");
		} else {
			printf("NO\n");
			st->clear(st);
		}
	}
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(fd != NULL)
		fclose(fd);
	if(st != NULL)
		st->destroy(st);
	return exitStatus;
}
