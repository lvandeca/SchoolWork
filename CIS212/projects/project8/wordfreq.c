#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include "sort.h"
#include "ADTs/hashcskmap.h"
#include "ADTs/stringADT.h"
#include "ADTs/arraylist.h"

int keycmp(void *x1, void *x2) {
	MEntry *m1 = (MEntry *)x1;
	MEntry *m2 = (MEntry *)x2;
	return strcmp((char *)m1->key, (char *)m2->key);
}

int invertkeycmp(void *x1, void *x2) {
	MEntry *m1 = (MEntry *)x1;
	MEntry *m2 = (MEntry *)x2;
	return (strcmp((char *)m1->key, (char *)m2->key) * -1);
}
int valuecmp(void *x1, void *x2) {
	MEntry *m1 = (MEntry *)x1;
	MEntry *m2 = (MEntry *)x2;
	return (long)m1->value < (long)m2->value;
}
int invertvaluecmp(void *x1, void *x2) {
	MEntry *m1 = (MEntry *)x1;
	MEntry *m2 = (MEntry *)x2;
	return (long)m1->value > (long)m2->value;
}

void fileClose(void *x) {
	FILE *f = (FILE *)x;
	if(f != stdin && f != stdout && f != stderr)
		fclose(f);
}

void wordPerLine(const String *stADT, const ArrayList *words, bool punct, bool lower, FILE *fd) {
	char buf[BUFSIZ];

	//iterate through lines of file
	while(fgets(buf, BUFSIZ, fd) != NULL) {
		const ArrayList *al;
		long i;
		stADT->clear(stADT);

		//for each line, append to string, follow the option tags
		//for lower and punct, split into array with each element
		//of array being one word
		stADT->append(stADT, buf);
		if(lower)
			stADT->lower(stADT);
		if(punct)
			stADT->translate(stADT, "[:punct:]", ' ');
		al = stADT->split(stADT, "");
		if(al == NULL){
			continue;
		}

		//get each word in array (or each word on the current line
		//and add it to the bigger array that contains all the words
		//for the entire file
		for(i = 0; i < al->size(al); i++){
			char *s;
			(void) al->get(al, i, (void *)&s);
			char *perm = strdup(s);
			(void) words->add(words, (void *)perm);
		}
		al->destroy(al);
	}
}

void wordFrequency(const ArrayList *words, const CSKMap *map) {
	
	//iterate through all the words in the file
	const Iterator *it = words->itCreate(words);
	while(it->hasNext(it)) {
		char *w;
		long frequency = 0L;
		(void) it->next(it, (void **)&w);

		//check if word is already a key in the map
		//if so, get its frequency, and increment it		
		if(map->get(map, w, (void **)&frequency))
			frequency++;

		//word is not in map, set frequency to one
		else
			frequency = 1L;

		//if word was already in map, it is replaced with increased frequency
		//otherwise, word is added to map with frequency of 1
		map->put(map, w, (void *)frequency);
	}
	it->destroy(it);
}

void printFrequency(const CSKMap *map, bool invert, bool sortAlpha, bool sortFreq) {

	//if neither sort option is provided, simply iterate 
	//through map printing the frequency and word
	if(!sortAlpha && !sortFreq) {
		const Iterator *mit = map->itCreate(map);
		while(mit->hasNext(mit)) {
			MEntry *me;
			(void) mit->next(mit, (void**)&me);
			printf("%8ld %s\n", (long)me->value, me->key);
		}
		mit->destroy(mit);
	} else {
		//set the correct compare function for the sort
		int (*cmpFunction)(void*, void*);
		if(invert) {
			if(sortAlpha)
				cmpFunction = &invertkeycmp;
			if(sortFreq)
				cmpFunction = &invertvaluecmp;
		} else {
			if(sortAlpha)
				cmpFunction = &keycmp;
			if(sortFreq)
				cmpFunction = &valuecmp;
		}
		
		//generate array of MEntry pairs, store length in n
		//and sort the array depending on compare function
		long i, n;
		MEntry **mes = map->entryArray(map, &n);
		sort((void **)mes, n, *cmpFunction);
		
		//iterate through sorted array, print the frequency and word
		for(i = 0L; i < n; i++) {
			printf("%8ld %s\n", (long)mes[i]->value, mes[i]->key);
		}
		free((void *)mes);
	}
}

int main(int argc, char **argv) {
	bool punct = false;
	bool lower = false;
	bool invert = false;
	bool sortAlpha = false;
	bool sortFreq = false;

	int exitStatus = EXIT_FAILURE;
	int opt;

	const String *stADT;
	const ArrayList *alFiles;
	const ArrayList *words;
	const CSKMap *map;
	
	//failure to create stADT (StringADT)
	if((stADT = String_create("")) == NULL) {
		fprintf(stderr, "%s: Unable to create String instance\n", argv[0]);
		goto cleanup;
	}
	
	//failure to create alFiles (ArrayListADT)
	if((alFiles = ArrayList_create(0L, fileClose)) == NULL) {
		fprintf(stderr, "%s: Unable to create ArrayList of FILE*'s\n", argv[0]);
		goto cleanup;
	}

	//failure to create words (ArrayListADT)
	if((words = ArrayList_create(0L, free)) == NULL) {
		fprintf(stderr, "%s: Unable to create ArrayList of words\n", argv[0]);
		goto cleanup;
	}

	//failure to create map (HashCSKMapADT)
	if((map = HashCSKMap(0L, 0.0, NULL)) == NULL) {
		fprintf(stderr, "%s: Unable to create Hash Map instance \n", argv[0]);
		goto cleanup;
	}
	
	//process the options
	opterr = 0;
	while((opt = getopt(argc, argv, "afpli")) != -1) {
		switch(opt) {
			case 'a': sortAlpha = true; break;
			case 'f': sortFreq = true; break;
			case 'p': punct = true; break;
			case 'l': lower = true; break;
			case 'i': invert = true; break;
			default:
				  fprintf(stderr, "%s: invalid option '-%c'\n", argv[0], optopt);
				  fprintf(stderr, "Usage: %s [-afpli] [FILE...]\n", argv[0]);
				  goto cleanup;
		}
	}

	//generate error if sort -a and -f are input
	if(sortAlpha && sortFreq) {
		fprintf(stderr, "invalid option combination: -af\n");
		goto cleanup;

	//generate error if invert -i without a sort input -a or -f
	} else if(invert && (!sortAlpha && !sortFreq)) {
		fprintf(stderr, "invalid option combination: -i without either -a or -f\n");
		goto cleanup;
	}

	FILE *fd = NULL;
	int i;

	//no file input, read from standard input
	if(optind >= argc) {
		(void) alFiles->add(alFiles, (void *)stdin);
	
	//file(s) input, open all and add them to alFiles
	} else {
		for(i = optind; i < argc; i++) {
			if((fd = fopen(argv[i], "r")) == NULL) {
				fprintf(stderr, "%s: Unable to open file: %s\n", argv[0], argv[i]);
				goto cleanup;
			}
			(void) alFiles->add(alFiles, (void *)fd);
		}	
	}

	//iterate through all files, print word frequency table for each
	for(i = 0; alFiles->get(alFiles, (long)i, (void **)&fd); i++) {
		wordPerLine(stADT, words, punct, lower, fd);
		wordFrequency(words, map);
		words->clear(words);
	}
	printFrequency(map, invert, sortAlpha, sortFreq);
	exitStatus = EXIT_SUCCESS;

cleanup:
	if(stADT != NULL)
		stADT->destroy(stADT);
	if(alFiles != NULL)
		alFiles->destroy(alFiles);
	if(map != NULL)
		map->destroy(map);
	if(words != NULL)
		words->destroy(words);
	return exitStatus;
}
