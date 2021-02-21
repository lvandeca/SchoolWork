#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "stsplit.h"

void printLWC(char *name, bool flags[], long counts[]){
	int i;
	//char *j;

	for(i = 0; i < 3; i++){
		if(flags[i])
			printf("%8ld ", counts[i]);
	}
	printf(name);
	printf("\n");

}

void countLWC(FILE *fd, long *nl, long *nw, long *nc){
	char buf[BUFSIZ];
	char *p = NULL;
	int i;

	while(fgets(buf, sizeof buf, fd) != NULL){
		(*nl)++;
		char **words = stsplit(buf);
		for (i = 0; words[i] != NULL; i++){
			(*nw)++;
		}
		for (p = &buf[0]; *p != '\0'; p++){
			(*nc)++;
		}
		stfree(words);
	}
}

int main(int argc, char *argv[]){
	long nlines = 0L;
	long nwords = 0L;
	long nchars = 0L;
	int opt;
	bool doChar, doLine, doWord, haveFlag;
	FILE *fp;
	int i;



	doChar = doLine = doWord = haveFlag = false;
	opterr = 0;

	while ((opt = getopt(argc, argv, "clw")) != -1) {
		switch(opt){
			case 'c': doChar = haveFlag = true; break;
			case 'l': doLine = haveFlag = true; break;
			case 'w': doWord = haveFlag = true; break;
			default: fprintf(stderr, "%s: illegal option, '%c'\n", argv[0], optopt);
		}
	}

	if(!haveFlag)
		doChar = doLine = doWord = true;

	bool flags[] = {doLine, doWord, doChar};
	char *empty = " ";

	if ((argc > 1)){
		//printf("Got inside main if(argc > 1)\n");
		if(!haveFlag){
			//printf("Hit the !haveFlag if statement\n");
			for(i = 1; i < argc; i++){
				fp = fopen(argv[i], "r");
				if (fp == NULL){
					fprintf(stderr, "%s: open(%s) error\n", argv[0], argv[i]);
					return EXIT_FAILURE;
				}
				//printf("no flags\n");
				countLWC(fp, &nlines, &nwords, &nchars);
				
				long counts[] = {nlines, nwords, nchars};
				printLWC(argv[i], flags, counts);
				fclose(fp);
			}
		}
		else if(haveFlag) {
			//printf("hit the haveFlag if statment\n");
			for(i = 2; i < argc; i++){
				fp = fopen(argv[i], "r");
				if (fp == NULL){
					fprintf(stderr, "%s: open(%s) error\n", argv[0], argv[i]);
					return EXIT_FAILURE;
				}
				//printf("with flags\n");
				countLWC(fp, &nlines, &nwords, &nchars);

				long counts[] = {nlines, nwords, nchars};
				printLWC(argv[i], flags, counts);
				fclose(fp);
			}
		}
		else{
			//printf("this is for <filename with flags\n");
			countLWC(stdin, &nlines, &nwords, &nchars);

			long counts[] = {nlines, nwords, nchars};
			printLWC(empty, flags, counts);
		}
	}
	else{
		printf("this is for <file with no flags\n");
		countLWC(stdin, &nlines, &nwords, &nchars);

		long counts[] = {nlines, nwords, nchars};
		printLWC(empty, flags, counts);
	}
		
	
	return EXIT_SUCCESS;
}
