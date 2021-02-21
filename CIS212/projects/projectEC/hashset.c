#include "hashset.h"  /* the .h file does NOT reside in /usr/local/include/ADTs */
#include <stdlib.h>
/* any other includes needed by your code */
#define UNUSED __attribute__((unused))

#define DEFAULT_CAPACITY 16			//if input capacity is 0
#define MAX_CAPACITY 134217728L			
#define DEFAULT_LOAD_FACTOR 0.75		//load factor if none is input
#define TRIGGER 100				//number of changes to resize bucket array

typedef struct node {
	struct node *next;
	void *value;
}Node;

typedef struct s_data {
    /* definitions of the data members of self */

	void (*freeV)(void *v);
	int (*cmp)(void *first, void *second);
	long size, capacity, changes;
	double load, loadFactor, increment;
	Node **buckets;
	long (*hash)(void *, long N);
} SData;

/*
 * important - remove UNUSED attributed in signatures when you flesh out the
 * methods
 */

static void purge(SData *sd, void (*freev)(void *v)) {
	/* helper function to apply freeV to all the elements hash table */
	long i;

	for(i = 0L; i < sd->capacity; i++) {
		Node *p, *q;
		p = sd->buckets[i];
		while(p != NULL) {
			(*freev)(p->value);
			q = p->next;
			free(p);
			p = q;
		}
		sd->buckets[i] = NULL;
	}
}

static void s_destroy(const Set *s) {
    /* implement the destroy() method */

	SData *sd = (SData *)s->self;
	purge(sd, sd->freeV);
	free(sd->buckets);
	free(sd);
	free((void *)s);
    return;
}

static void s_clear(const Set *s) {
    /* implement the clear() method */

	SData *sd = (SData *)s->self;
	purge(sd, sd->freeV);
	sd->size = 0L;
	sd->load = 0.0;
	sd->changes = 0L;
    return;
}

static Node *findValue(SData *sd, void *value, long *bucket) {
	/* helper function to find value hash table */
	long i = sd->hash(value, sd->capacity);				//apply hash function to value. store in i
	Node *p;

	*bucket = i;							//set the bucket to hash value returned
	for(p = sd->buckets[i]; p != NULL; p = p->next) {		//iterate through linked list at buckets[i] 
		if(sd->cmp(p->value, value) == 0) {			//apply compare function to determine if value is in linked list
			break;
		}
	}
	return p;
}

static void resize(SData *sd) {
	/* helper function to create larger array of buckets */
	long N;
	Node *p, *q, **array;
	long i, j;

	N = 2 * sd->capacity;						//double the size of the array
	if(N > MAX_CAPACITY)						//check that the array doesn't exceed MAX_CAPACITY
		N = MAX_CAPACITY;
	if(N == sd->capacity)						//if array is already at max size, return
		return;
	array = (Node **)malloc(N * sizeof(Node *));			//allocate memory for new bucket array
	if(array == NULL)
		return;
	for (j = 0L; j < N; j++) {
		array[j] = NULL;
	}

	for(i = 0L; i < sd->capacity; i++) {				//iterate through bucket array, placing values in new array
		for(p = sd->buckets[i]; p != NULL; p = q) {
			q = p->next;
			j = sd->hash(p->value, N);
			p->next = array[j];
			array[j] = p;
		}
	}
	free(sd->buckets);						//free bucket array
	sd->buckets = array;						//replace bucket with new array
	sd->capacity = N;						//change capacity to N (or new capacity)
	sd->load /= 2;							//we doubled size of the array, so half the load 
	sd->changes = 0.0;						//reset changes
	sd->increment = 1.0/(double)N;					//new increment cause capacity (N) is larger
}

static int insertEntry(SData *sd, void *value, long i) {
	/* helper function for inserting new value into correct linked list bucket */
	Node *p = (Node *)malloc(sizeof(Node));
	int status = 0;

	if(p != NULL) {
		p->value = value;
		p->next = sd->buckets[i];				//new value inserted at the head, p points to old head
		sd->buckets[i] = p;					//new head of bucket becomes p
		sd->size++;
		sd->load += sd->increment;
		sd->changes++;
		status = 1;
	}
	return status;
}

static int s_add(const Set *s, void *member) {
    /* implement the add() method */

	SData *sd = (SData *)s->self;
	long i;
	Node *p;
	int status = 0;

	if((sd->changes) > TRIGGER) {					//if the number of changes is larger then the trigger
		sd->changes = 0;
		if((sd->load) > (sd->loadFactor)) {			//and the load is larger then the input loadFactor
			resize(sd);					//resize the bucket array, double the size if not larger then max
		}
	}

	p = findValue(sd, member, &i);					//determine if the value is already in set
	if(p == NULL) {							//if not, insert it into the set
		status = insertEntry(sd, member, i);
	}

    return status;
}

static int s_contains(const Set *s, void *member) {
    /* implement the contains() method */

	SData *sd = (SData *)s->self;
	long bucket;

    return (findValue(sd, member, &bucket) != NULL);			//return true if findValue does not return a NULL pointer
}

static int s_isEmpty(const Set *s) {
    /* implement the isEmpty() method */

	SData *sd = (SData *)s->self;
    return (sd->size == 0L);
}

static int s_remove(const Set *s, void *member) {
    /* implement the remove() method */

	SData *sd = (SData *)s->self;
	long i;
	Node *entry;
	int status = 0;

	entry = findValue(sd, member, &i);				//determine if the member is int the set, if so, proceed
	if(entry != NULL) {
		Node *p, *c;
		for(p = NULL, c = sd->buckets[i]; c != entry; p = c, c = c->next)
			;						//find where the member is in the bucket[i]
		if(p == NULL)						//if p == NULL, then the member is the head of the bucket
			sd->buckets[i] = entry->next;			//set head to be the next member in the bucket
		else							//else p != NULL, entry is some member in the bucket
			p->next = entry->next;				//set p (the member before entry) to point to member after entry
		sd->size--;						
		sd->load -= sd->increment;
		sd->changes++;
		sd->freeV(entry->value);				//apply freeV to entry member (i.e. remove entry)
		free(entry);						//free (aka remove) entry
		status = 1;
	}

    return status;
}

static long s_size(const Set *s) {
    /* implement the size() method */

	SData *sd = (SData *)s->self;
    return sd->size;
}

static void **createArray(SData *sd) {
	void **tmp = NULL;
	if(sd->size > 0L) {
		size_t nbytes = sd->size * sizeof(void *);		//determine number of bytes needed for array
		tmp = (void **)malloc(nbytes);
		if(tmp != NULL) {
			long i, N = 0L;
			for(i = 0L; i < sd->capacity; i++) {		//iterate over all the buckets
				Node *p = sd->buckets[i];
				while(p != NULL) {			//iterate over all the nodes in the linked list
					tmp[N++] = p->value;		//place value from each node into the array
					p = p->next;			
				}
			}
		}
	}

	return tmp;
}

static void **s_toArray(const Set *s, long *len) {
    /* implement the toArray() method */

	SData *sd = (SData *)s->self;
	void **tmp = createArray(sd);					//create the array
	if(tmp != NULL) {
		*len = sd->size;					//if arrayCreate does not fail, set length to the size of the Set
	}
    return tmp;
}

static const Iterator *s_itCreate(UNUSED const Set *s) {
    /* implement the itCreate() method */
	
	SData *sd = (SData *)s->self;
	const Iterator *it = NULL;	
	void **tmp = createArray(sd);					//create the array

	if(tmp != NULL) {						//if arrayCreate does not fail create an instance of an Iterator
		it = Iterator_create(sd->size, tmp);			//with tmp as the array	and size of Set as the length
		if(it == NULL) {					//check if instance creation failed, then free the array
			free(tmp);
		}
	}
    return it;
}

static UNUSED Set template = {
    NULL, s_destroy, s_clear, s_add, s_contains, s_isEmpty, s_remove,
    s_size, s_toArray, s_itCreate
};

void doNothing(UNUSED void *x){
	/* helper function that does nothing */
}

const Set *HashSet(void (*freeValue)(void*), int (*cmpFxn)(void*, void*), long capacity, double loadFactor, long (*hashFxn)(void *m, long N)) {
    /* construct a Set instance and return to the caller */

	Set *s = (Set *)malloc(sizeof(Set));
	long N;
	double lf;
	Node **array;
	long i;

	if(s != NULL) {											//check that malloc worked for Set
		SData *sd = (SData *)malloc(sizeof(SData));

		if(sd != NULL) {									//check that malloc worked for SData
			N = ((capacity > 0) ? capacity : DEFAULT_CAPACITY);				//check if input capacity is 0, then set to DEFAULT_CAPACITY
			N = ((N > MAX_CAPACITY) ? MAX_CAPACITY : N);					//check if input capacity is bigger then MAX_CAPACITY
			lf = ((loadFactor > 0.000001) ? loadFactor : DEFAULT_LOAD_FACTOR);		//check if input loadFactor is 0, then set to DEFAULT_LOAD_FACTOR
			array = (Node **)malloc(N * sizeof(Node *));					//allocate memory for the array of buckets

			if(array != NULL) {								//check that malloc worked for array
				sd->capacity = N; sd->size = 0L; sd->changes = 0L;			//set capacity, size, changes
				sd->load = 0.0; sd->loadFactor = lf; sd->increment = 1.0 / (double)N;	//set load, loadFactor, increment
				sd->hash = hashFxn; sd->cmp = cmpFxn;					//set hash and compare function
				sd->freeV = ((freeValue == NULL) ? doNothing : freeValue);		//check in input freeValue function is NULL, if so doNothing
				sd->buckets = array;							//set array of buckets to array
				for(i = 0L; i < N; i++) {
					array[i] = NULL;						//initialize array of bucket pointer to NULL
				}
				*s = template;
				s->self = sd;
			} else {
				free(sd); free(s); s = NULL;
			}
		} else {
			free(s); s = NULL;
		}
	}
    return s;
}
