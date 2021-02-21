#include "stringlist.h"
#include "stdlib.h"

typedef struct sldata {          /* data for each instance */
    /* you must define the instance-specific fields for each StringList */
	 long capacity;
	 long size;
	 char **theArray;
} SLData;

/* any helper functions needed by the methods */

static void sl_destroy(const StringList *sl) {
    SLData *sld = (SLData *)sl->self;

    /* the body of the destroy() method */
    long size = sld->size;
    if(size > 0L) {
	long i;

	for(i = 0L; i < size; i++){
		free(sld->theArray[i]);
	}
    }

    free(sld->theArray);
    free(sld);
    free((void *)sl);
}

static int sl_append(const StringList *sl, char *s) {
    SLData *sld = (SLData *)sl->self;

    /* the body of the append() method - it must grow the capacity of
       the stringlist if you have run out of room */
    int status = (sld->capacity > sld->size);

    if(!status){
	size_t nbytes = (2 * sld->capacity * sizeof(char*));
	char **tmp = (char **)realloc(sld->theArray, nbytes);
	if(tmp != NULL){
		status = 1;
		sld->theArray = tmp;
		sld->capacity *= 2;
	}
    }
    if(status){
	sld->theArray[sld->size++] = s;
    }
    return status;
}

static int sl_get(const StringList *sl, long index, char **sptr) {
    SLData *sld = (SLData *)sl->self;

    /* the body of the get() method */
    int status = (index >= 0L && index < sld->size);

    if(status){
	*sptr = sld->theArray[index];
    }
    return status;
}

static long sl_size(const StringList *sl) {
    SLData *sld = (SLData *)sl->self;

    /* the body of the size() method */
    return sld->size;
}

static StringList template = {
    NULL, sl_destroy, sl_append, sl_get, sl_size
};

const StringList *StringList_create(long capacity) {/* use default if 0L */

    /* the body of the constructor */
	StringList *sl = (StringList *)malloc(sizeof(StringList));
	if(sl != NULL){
		SLData *sld = (SLData *)malloc(sizeof(SLData));
		if(sld != NULL){
			long cap = (capacity <= 0L) ? DEFAULT_CAPACITY : capacity;
			char **theArray = (char **)malloc(cap * sizeof(char*));
			if(theArray != NULL){
				sld->capacity = cap;
				sld->size = 0L;
				sld->theArray = theArray;
				*sl = template;
				sl->self = sld;
			} else {
				free(sld);
				free(sl);
				sl = NULL;
			}
		} else {
			free(sl);
			sl = NULL;	
		}
	}
	return sl;
}
