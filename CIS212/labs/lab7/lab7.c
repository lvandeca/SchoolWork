#include "ADTs/stack.h"
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

void palindrome(FILE *fd, const Stack *st) {
	char buf[BUFSIZ];
	while(fgets(buf, BUFSIZ, fd) != NULL){
		int i;
		int len = strlen(buf) - 1;
		int mid = len/2;
		bool isPalindrome = false;

		// Step-1: Push each character onto the Stack
		for(i = 0; i < mid; i++) {
			char c = buf[i];
			(void) st->push(st, (void *)(long)c);
		}

		if(len % 2 != 0) {
			i++;
		}
		
		// Step-2: Pop the characters and compare to the buffer
		while(buf[i] != '\n') {
			isPalindrome = true;
			char c;
			st->pop(st, (void **)&c);

			if(c != buf[i]){
				isPalindrome = false;	
			}
			i++;

		}

		// Step-3: Print the answer
		if(isPalindrome) {
			fprintf(stdout, "Its a Palindrome! Word: %s\n", buf);
		} else {
			fprintf(stdout, "Not a Palindrome :( Word: %s\n", buf);
		}
	}	
}


int main(int argc, char *argv[]){
	FILE * fd = NULL;
	const Stack *st = Stack_create(free);
	int exitStatus = EXIT_FAILURE;

	if(argc != 2){
		fprintf(stderr, "Incorrect usage. Usage: %s file\n", argv[0]);
		goto cleanup;
	}

	if((fd = fopen(argv[1], "r")) == NULL){
		fprintf(stderr, "Unable to open given file: %s\n", argv[1]);
		goto cleanup;
	}

	if(st == NULL) {
		fprintf(stderr, "Cannot creat the stackADT...\n");
		goto cleanup;	
	}

	palindrome(fd, st);

	exitStatus = EXIT_SUCCESS;


cleanup:
	if(st != NULL)
		st->destroy(st);
	if(fd != NULL)
		fclose(fd);
	return exitStatus;
}
