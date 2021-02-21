/* ./wordperline [OPTIONS]... [FILE]... */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>

#include "ADTs/stringADT.h"
#include "ADTs/arraylist.h"

typedef struct my_file{
	FILE *f;
	char name[256];
} MyFile;

void wordperline(MyFile files[], int nFiles, bool toLower, bool punctSeperate) {
	char buf[BUFSIZ];
	int i;

	for (i = 0; i < nFiles; i++) {
		while(fgets(buf, BUFSIZ, files[i].f) != NULL) {
			//initialize line into string
			const String *str = String_create(buf);
			
			// perform actions for options
			if(toLower)
				str->lower(str);
			if(punctSeperate)
				str->translate(str, "[:punct:]", ' ');
			
			//stadanrd splitting of words
			str->translate(str, "[:space:]", ' ');
			
			//proces string and print
			const ArrayList *file = str->split(str, " ");
			const Iterator *it = file->itCreate(file);
			while(it->hasNext(it)) {
				char *temp;
				char *blank = "";
				(void) it->next(it, (void **)&temp);
				if(strcmp(temp, blank)){ 
					printf("%s\n", temp);
				}
			}
			it->destroy(it);
			file->destroy(file);
			str->destroy(str);
		}
	}
}

int main(int argc, char *argv[]) {
	int opt;
	int exitStatus = EXIT_FAILURE;
	MyFile files[100];
	bool toLower, punctSeperate;

	toLower = punctSeperate = false;
	opterr = 0;

	while((opt = getopt(argc, argv, "lp")) != -1) {
		switch(opt) {
			case 'l': toLower = true; break;
			case 'p': punctSeperate = true; break;
			
			default:
				  fprintf(stderr, "%s: invalid option '-%c'\n", argv[0], optopt);
				  goto cleanup;
		}
	}

	int nFiles = 0;
	int i;
	for(i = optind; i < argc; i++){
		FILE *fd = fopen(argv[i], "r");
		if(fd == NULL) {
			fprintf(stderr, "%s: unable to open file: %s\n", argv[0], argv[i]);
			goto cleanup;
		}
		files[nFiles].f = fd;
		strcpy(files[nFiles].name, argv[i]);
		nFiles++;
	}

	if(nFiles == 0) {
		files[nFiles].f = stdin;
		strcpy(files[nFiles++].name, "");
	}

	wordperline(files, nFiles, toLower, punctSeperate);
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(nFiles > 0) {
		for(i = 0; i<nFiles; i++)
			if(files[i].f != stdin)
				fclose(files[i].f);
	}
	return exitStatus;
}

