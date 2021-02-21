/* ./sgrep [OPTION] ...STRING[FILE] */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

void sgrep(FILE *fd, char *filename, bool ignoreCase, bool invert, bool printCount, bool multipleFiles, char *string){
	char buf[BUFSIZ];
	char bufcpy[BUFSIZ];
	char stringcpy[sizeof string];
	int notmatchLines, matchLines, totalLines;
	int i, j;

	notmatchLines = matchLines = totalLines = 0;

	while (fgets(buf, BUFSIZ, fd) != NULL){
		totalLines++;
		
		// change all characters to lower case if -i option is input
		if(ignoreCase){
			for(i = 0; i < BUFSIZ; i++){
				bufcpy[i] = tolower(buf[i]);
			}
			for(j = 0; j < sizeof string; j++){
				stringcpy[j] = tolower(string[j]);
			}	
		}

		// check if lines match
		if (invert){
			if(ignoreCase){
				if (strstr(bufcpy, stringcpy) == NULL){
					notmatchLines++;

					// if -c is not input, print the line that contains the string
					if (!printCount){
						if(multipleFiles)
							printf("%s:", filename);
						printf("%s", buf);
					}
				}
			} else{
				if (strstr(buf, string) == NULL){
					notmatchLines++;

					if(!printCount){
						if(multipleFiles)
							printf("%s:", filename);
						printf("%s", buf);
					}
			}
		}
		// if -v is input, check if not matchiing line
		}
		else {
			if(ignoreCase){
				if (strstr(bufcpy, stringcpy) != NULL){
					matchLines++;
			
					// if -c is not input, print the corresponding non-matching line
					if (!printCount){
						if(multipleFiles)
							printf("%s:", filename);
						printf("%s", buf);
					}
				}
			} else{
				if (strstr(buf, string) != NULL){
					matchLines++;
					if (!printCount){
						if(multipleFiles)
							printf("%s:", filename);
						printf("%s", buf);
					}
				}
			}
		}
		
	}

	// if -c option, print the number of lines that either match or don't
	if (printCount){
		if(invert){
			if(multipleFiles)
				printf("%s:", filename);
			printf("%d\n", notmatchLines);
		}
		else{
			if(multipleFiles)
				printf("%s:", filename);
			printf("%d\n", matchLines);
		}
	}
}

int main(int argc, char *argv[]){
	int opt, totalF;
	bool ignoreCase, invert, printCount, haveFlag, multipleFiles;
	int exitStatus = EXIT_SUCCESS;

	opterr = 0;
	ignoreCase = invert = printCount = haveFlag = multipleFiles = false;

	// check input of cases
	while((opt = getopt(argc, argv, "ivc")) != -1){
		switch(opt){
			case 'i': ignoreCase = haveFlag = true; break;
			case 'v': invert = haveFlag = true; break;
			case 'c': printCount = haveFlag = true; break;
			default: fprintf(stderr, "%s: illegal option, '%c'\n", argv[0], optopt);
				 return EXIT_FAILURE;
		}
	}
		
	totalF = argc - optind;
	int i;

	if (totalF == 0){
		fprintf(stderr, "%s: No string provided\n", argv[0]);
		exitStatus = EXIT_FAILURE;
		goto cleanup;
	}
	else if(totalF == 1) {
		sgrep(stdin, NULL, ignoreCase, invert, printCount, multipleFiles, argv[optind]);	
	}
	else{
		for (i = (optind + 1); i < argc; i++){
			if (strcmp(argv[i], "-") == 0){
					sgrep(stdin, NULL, ignoreCase, invert, printCount, multipleFiles, argv[optind]);
			} else {
				FILE *fd = fopen(argv[i], "r");
				if (fd == NULL){
					fprintf(stderr, "%s: open(%s) error\n", argv[0], argv[i]);
					exitStatus = EXIT_FAILURE;
					goto cleanup;
				}
				else if(totalF >= 3){
					multipleFiles = true;
					sgrep(fd, argv[i], ignoreCase, invert, printCount, multipleFiles, argv[optind]);
				} else{
					sgrep(fd, NULL, ignoreCase, invert, printCount, multipleFiles, argv[optind]);
				}
				fclose(fd);
			}
		}	
	}
cleanup:
	return exitStatus;
}
