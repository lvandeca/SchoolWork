#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "stsplit.h"

void filter(char *line, char *output, int lineNum, char *remWord, char remChar, bool doWord, bool doChar){
	char **words = stsplit(line);
	int i, count;
	unsigned long j;
	char space[1] = {" "};
	char newline[strlen(line)];
	sprintf(output, "%2d: ", lineNum);

	count = 0;
	for(i = 0; words[i] != NULL; i++) {
		if(doWord == false || strcmp(words[i], remWord) != 0) {
			strcpy(newline, words[i]);
			strncat(newline, space, 1);
		} else if (words [i + 1] != NULL) {
			strncat(newline, words[i], strlen(words[i]));
			strncat(newline, space, 1);
		} else {
			strncat(newline, words[i], strlen(words[i]));
		}
		count++;
	}

	for(j=0; j<strlen(newline); j++) {
		if(doChar == false || remChar != newline[j]) {
			strncat(output, &newline[j], 1);
		}
	}

	int len = strlen(output);
	output[len] = '\0';
	stfree(words);
}

int main(int argc, char *argv[]) {
	int option;
	char remChar;
	char *remWord = NULL;
	char buf[BUFSIZ];
	char output[BUFSIZ];
	extern int opterr;
	bool doWord, doChar;
	bool start = true;
	int exitStatus;
	int i;
	opterr = 0;
	doWord = doChar = false;

	while ((option = getopt(argc, argv, "c:w:")) != -1) {
		switch(option) {
			case 'c': remChar = *optarg; doChar = true; break;
			case 'w': remWord = optarg; doWord = true; break;
			default:
				  printf("Unknown flag: -%c\n", optopt);
				  start = false;
				  break;
		}
	}

	remWord = NULL;
	if(start) {
		i = 1;
		while(fgets(buf, BUFSIZ, stdin) != NULL) {
			filter(buf, output, i, remWord, remChar, doWord, doChar);
			fprintf(stdout, "%s\n", output);
			i++;
		}
		exitStatus = EXIT_SUCCESS;
	} else {exitStatus = EXIT_FAILURE;}

	return exitStatus;
}
