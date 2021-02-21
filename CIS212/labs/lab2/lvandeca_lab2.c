#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define UNUSED __attribute__((unused))
#define BUFSIZE 1024

int main(int argc, char *argv[]) {
	
	int option;
	int r = 0;
	char rem;
	extern int opterr;
	opterr = 0;

	//Parse command line argument
	while((option = getopt(argc, argv, "r:")) != -1 ) {
		switch(option) {
			case 'r':
				rem = *optarg;
				printf("Caught a wild -%c\n", option);
				r = 1;
				break;
			case '?':
				printf("Unknown Flag: -%c\n", option);
				break;
		}
	}

	char buf[BUFSIZE];
	int i = 0;
	int j;

	while (fgets(buf, BUFSIZE, stdin) != NULL) {
		if(r) {
			for(j=0; j<strlen(buf); j++) {
				if(buf[j] == rem) {
					buf[j] = ' ';
				}
			}	
		}
		printf("%d: %s\n", i, buf);
		i++;
	}

	return EXIT_SUCCESS;
}
