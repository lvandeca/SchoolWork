#include <stdio.h>
#include <stdlib.h>
#include "ADTs/stringADT.h"
#include "ADTs/arraylist.h"
#include <stdbool.h>
#include <unistd.h>
#include <math.h>

#define USESTR "usage: %s [-as] [FILE] ...\n"


void getStats(bool doStat) {
	if(doStat) {
		 return;
	}
}


int main(int argc, char *argv[]) {

	int opt;
	FILE * fp;

	bool doStat = false;

	opterr = 0;
	while((opt = getopt(argc, argv, "s")) != -1) {
		switch(opt) {
			case 's':
				doStat = true;
				break;
			default:
				fprintf(stderr, "%s: invalid option '-%c'\n", argv[0], optopt);
				fprintf(stderr, USESTR, argv[0]);
				return EXIT_FAILURE;
		}
	}

	fp = fopen(argv[optind], "r");
	if(fp == NULL) {
		fprintf(stderr, "%s: unable to open file: %s\n", argv[0], argv[optind]);
		return EXIT_FAILURE;
	}
	
	getStats(doStat);
}
