#include <unistd.h>	/* for getopt(), opterr, optind, and aoptopt */
#include <stdio.h>	/* for fprintf() and stderr*/
#include <stdlib.h>	/* for EXIT_SUCCESS and EXIT_FAILURE */
#include <stdbool.h>	/* for bool, true, and false */
#include <string.h>

int main(int argc, char *argv[]){
	int opt;
	bool doChar, doLine, doWord, haveFlag;

	doChar = doLine = doWord = haveFlag = false;
	opterr = 0; /* tells getopt to NOT print an illegal option error message */
	while((opt = getopt(argc, argv, "clw")) != -1) {
		switch(opt) {
			case 'c': doChar = haveFlag = true; break;
			case 'l': doLine = haveFlag = true; break;
			case 'w': doWord = haveFlag = true; break;
			default: fprintf(stderr, "%s: illegal option, '-%c'\n", argv[0], optopt);
				 /* complete error processing */
		}
	}
	if (! haveFlag) { /* handle default */
		doChar = doLine = doWord = true;
	}
	/* at this point, optind is the index into argv[] for the first non-opton */
	/* process files using doChar, doLine, and doWord booleans */

	if(doLine){printf("Counting lines\n");}
	if(doWord){printf("Counting words\n");}
	if(doChar){printf("Counting character\n");}

	int i;
	int j;
	char ch[BUFSIZ];
	strcpy(ch, "");

	if ((argc == 1)){printf("Processing standard input and no total line\n");}
	if ((argc == 2)){
		if (haveFlag)
			printf("Processing standard input and no total line\n");
		else
			printf("Processing %s and no total line\n", argv[1]);
	}
	if ((argc == 3)){printf("Processing %s and no total line\n", argv[2]);}
	if ((argc > 3)){
		if(!haveFlag){
			for (i = 1; argv[i] != NULL; i++){
				strcat(ch, argv[i]);
				strcat(ch, ", ");
			}
		}
		else{
			for (j = 2; argv[j] != NULL; j++){
				strcat(ch, argv[j]);
				strcat(ch, ", ");
			}
		}
		printf("Processing %sand a total line\n", ch);
	}

	return EXIT_SUCCESS;

}
