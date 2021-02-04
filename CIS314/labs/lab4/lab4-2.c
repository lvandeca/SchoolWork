#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Person {
	char *first;
	char *last;
}Person;

char *readString(){
	
	char line[200];
	char *result = NULL;
	result = fgets(line, 200, stdin);
	if(result == NULL) {
		printf("Invalid input.\n");
		return 0;
	}
	int len = strlen(line);
	char *str = NULL;
	str = (char *)malloc(sizeof(char)*len);

	strncpy(str, line, len);
	str[len - 1] = '\0';

	return str;
}

int main() {
	struct Person *person = NULL;

	person = (struct Person*)malloc(sizeof(struct Person));

	printf("Enter person's first name: ");
	person->first = readString();

	printf("Enter person's last name: ");
	person->last = readString();

	printf("Persons full name: %s %s\n", person->first, person->last);

	free(person->first);
	free(person->last);
	free(person);

	return 0;
}
