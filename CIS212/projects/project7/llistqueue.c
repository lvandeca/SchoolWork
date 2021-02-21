/*
 * implementation for linked-list-based generic FIFO queue
 */

#include "ADTs/llistqueue.h"
#include <stdlib.h>
/* any other includes needed for the implementation */

typedef struct q_node {
    /* node data structure for linked list */
	struct q_node *next;
	void *value;
} QNode;

typedef struct q_data {
    /* flesh out the instance specific data structure */
	long size;
	void (*freeValue)(void *v);
	QNode *head;
	QNode *tail;
} QData;
/* any other data structures needed */

static void purge(QData *qd, void (*freeV)(void *v)) {
    /* free value function for nodes
     * helper funtion for q_destroy and q_clear*/
	if(freeV != NULL) {
		QNode *qn;
		for(qn = qd->head; qn != NULL; qn = qn->next)
			(freeV)(qn->value);
	}
}

static void freeList(QData *qd) {
    /* free node function
     * helper function for q_destroy and q_clear*/
	QNode *q, *n = NULL;
	for(q = qd->head; q != NULL; q = n) {
		n = q->next;
		free(q);
	}
}

static void q_destroy(const Queue *q) {
    /* implementation of the destroy() method */
	QData *qd = (QData *)q->self;
	purge(qd, qd->freeValue);
	freeList(qd);
	free(qd);
	free((void *)q);
}

static void q_clear(const Queue *q) {
    /* implementation of the clear() method */
	QData *qd = (QData *)q->self;
	purge(qd, qd->freeValue);
	freeList(qd);
	qd->head = qd->tail = NULL;
	qd->size = 0L;
}

static int q_enqueue(const Queue *q, void *element) {
    /* implementation of the enqueue() method */
	QData *qd = (QData *)q->self;
	QNode *new = (QNode *)malloc(sizeof(QNode));
	int status = (new != NULL);

	if(status) {
		new->value = element;
		new->next = NULL;
		if(qd->head == NULL) {
			qd->head = new;
		} else {
			qd->tail->next = new;
		}
		qd->tail = new;
		qd->size++;
	}

	return status;
}

static int q_front(const Queue *q, void **element) {
    /* implementation of the front() method */
	QData *qd = (QData *)q->self;
	int status = (qd->size > 0L);

	if(status) {
		*element = qd->head->value;
	}

	return status;
}

static int q_dequeue(const Queue *q, void **element) {
    /* implementation of the dequeue() method */
	QData *qd = (QData *)q->self;
	int status = (qd->size > 0L);

	if(status) {
		QNode *qn = qd->head;
		if((qd->head = qn->next) == NULL) {
			qd->tail = NULL;
		}
		*element = qn->value;
		qd->size--;
		free(qn);
	}

	return status;
}

static long q_size(const Queue *q) {
    /* implementation of the size() method */
	QData *qd = (QData *)q->self;
	return qd->size;
}

static int q_isEmpty(const Queue *q) {
    /* implementation of the isEmpty() method */
	QData *qd = (QData *)q->self;
	return (qd->size == 0L);
}

static void **genArray(QData *qd) {
    /* helper function for q_toArray and q_itCreate */
	void **theArray = NULL;
	if(qd->size >0L) {
		theArray = (void **)malloc(qd->size * sizeof(void *));
		if(theArray != NULL) {
			long i = 0L;
			QNode *qn;
			for(qn = qd->head; qn != NULL; qn = qn->next) {
				theArray[i++] = qn->value;
			}
		}
	}

	return theArray;
}

static void **q_toArray(const Queue *q, long *len) {
    /* implementation of the toArray() method */
	QData *qd = (QData *)q->self;
	void **tmp = genArray(qd);
	if(tmp != NULL) {
		*len = qd->size;
	}

	return tmp;
	
}

static const Iterator *q_itCreate(const Queue *q) {
    /* implementation of the itCreate() method */
	QData *qd = (QData *)q->self;
	const Iterator *it = NULL;
	void **tmp = genArray(qd);
	if(tmp != NULL) {
		it = Iterator_create(qd->size, tmp);
		if(it == NULL)
			free(tmp);
	}
	return it;
}

static const Queue *q_create(const Queue *q);
/* this is just declaring the signature for the create() method; it's
   implementation is provided below */

static Queue template = {
    NULL, q_create, q_destroy, q_clear, q_enqueue, q_front, q_dequeue, q_size,
    q_isEmpty, q_toArray, q_itCreate
};

static void doNothing(__attribute__((unused))void *e) {}

static const Queue *newQueue(void (*freeV)(void *e)) {
    /* helper function for q_create, LListQueue, and Queue_create */
	Queue *q = (Queue *)malloc (sizeof(Queue));

	if(q != NULL) {
		QData *qd = (QData *)malloc(sizeof(QData));
		
		if (qd != NULL) {
			qd->size = 0L;
			qd->head = NULL;
			qd->tail = NULL;
			qd->freeValue = (freeV != NULL) ? freeV : doNothing;
			*q = template;
			q->self = qd;
		} else {
			free(q);
			q = NULL;
		}
	}

	return q;
}

static const Queue *q_create(const Queue *q) {
    /* implementation of the create() method */
	QData *qd = (QData *)q->self;
	return newQueue(qd->freeValue);
}

const Queue *LListQueue(void (*freeValue)(void *e)) {
    /* implementation of the structure-specific constructor */
	return newQueue(freeValue);
}

const Queue *Queue_create(void (*freeValue)(void *e)) {
    /* implementation of the generic constructor */
	return newQueue(freeValue);
}
