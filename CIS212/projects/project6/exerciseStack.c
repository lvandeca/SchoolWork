#include "ADTs/stack.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printStack(const Stack *st, FILE *fd) {
	int i;
	long storePrint[BUFSIZ];
	
	//stack is not empty case
	if(!st->isEmpty(st)) {
		long print;

		//go through all items in the stack
		//pop item, print item, and store in list of longs
		for(i = 0; st->pop(st, (void **)&print); i++) {
			fprintf(stdout, "%s%ld", (i == 0) ? "" : " ", print);
			storePrint[i] = print;
		}
		printf("\n");

		//put items back into stack in original order
		while(i > 0) {
			i--;
			st->push(st, (void *)storePrint[i]);	
		}
	
	//stack is empty case
	} else {
		fprintf(fd, "Empty\n");
	}
}

int main(int argc, char *argv[]){
	FILE *fd = NULL;
	const Stack *st = Stack_create(free);
	int exitStatus = EXIT_FAILURE;
	long numlines;
	char *push = "push";
	char *pop = "pop";
	char *print = "print";
	char buf[BUFSIZ];

	if(argc != 2){
		fprintf(stderr, "Incorrect usage. Usage: %s file\n", argv[0]);
		goto cleanup;
	}

	if((fd = fopen(argv[1], "r")) == NULL) {
		fprintf(stderr, "Unable to open give file: %s\n", argv[1]);
		goto cleanup;
	}

	if(st == NULL){
		fprintf(stderr, "Cannot create stackADT...\n");
		goto cleanup;
	}

	fgets(buf, BUFSIZ, fd); 		//get number of lines from first line
	sscanf(buf, "%ld", &numlines);		//store number of lines in numlines

	while(numlines-- > 0) {
		fgets(buf, BUFSIZ, fd);			//iterate through lines
		char copybuf[BUFSIZ];;
		strcpy(copybuf, buf);
		char *instruction = strtok(buf, " \n");
		
		//if instruction is push, push the long value onto the stack
		if(!strcmp(instruction, push)) {
			char *storeString = strtok(copybuf, " ");
			storeString = strtok(NULL, " ");
			long N;
			sscanf(storeString, "%ld", &N);
			st->push(st, (void *)N);
		}
		
		//if instruction is pop, pop value on top of stack and print; if no value to be popped, print "StackError"
		if(!strcmp(instruction, pop)) {
			long popped;
			if(st->isEmpty(st)) {
				fprintf(stdout, "StackError\n");
			} else {
				st->pop(st, (void **)&popped);
				fprintf(stdout, "%ld\n", popped);
			}
		}

		//if instuction is print, print all items in the stack without popping them;
		//printStack will print "Empty" if stack is empty
		if(!strcmp(instruction, print)) {
			printStack(st, stdout);
		}	
	}
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(st != NULL)
		st->destroy(st);
	if(fd != NULL)
		fclose(fd);
	return exitStatus;
}
