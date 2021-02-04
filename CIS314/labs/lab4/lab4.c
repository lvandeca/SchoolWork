#include <stdio.h>
#include <stdlib.h>

int main() {
	
	char line[20];
	char *result = NULL;

	printf("Enter a number: ");
	result = fgets(line, 20, stdin);
	if(result == NULL){
		printf("Invalid input.\n");
		return 0;
	}

	long count = 0;
	char *endptr = NULL;
	count = strtol(line, &endptr, 10);
	if(line == endptr) {
		printf("Invalid input.\n");
		return 0;
	}

	int *number = NULL;
	number = (int *)malloc(sizeof(int) * count);
	
	int i;
	for(i = 0; i < count; i++) {
		number[i] = i + 1;
		// another way: 
		// *(numbers + i) i + 1;
	}

	for(i = 0; i < count; i++) {
		printf("%d ", number[i]);
	}

	printf("\n");
	free(number);

	return 0;
}
