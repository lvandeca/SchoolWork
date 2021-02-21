/*
 * Copyright (c) 2019, University of Oregon
 * All rights reserved.

 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:

 * - Redistributions of source code must retain the above copyright notice,
 *   this list of conditions and the following disclaimer.
 *
 * - Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * - Neither the name of the University of Oregon nor the names of its
 *   contributors may be used to endorse or promote products derived from this
 *   software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

/*
 * implementation for generic priority queue, for generic priorities
 * implemented using a singly-linked list, element sorted by priority
 */

#include "ADTs/llistprioqueue.h"
#include <stdlib.h>

typedef struct pqnode {
    struct pqnode *next;
    void *priority;
    void *value;
} PQNode;

typedef struct pq_data {
    int (*cmp)(void *p1, void *p2);
    long size;
    PQNode *head;
    PQNode *tail;
    void (*freePrio)(void *p);
    void (*freeValue)(void *v);
} PqData;

/*
 * traverses the list, calling freeP on each priority and freeV on each entry
 */
static void purge(PqData *pqd, void (*freeP)(void *p), void (*freeV)(void *e)) {
    if (freeP != NULL) {
        PQNode *p;

        for (p = pqd->head; p != NULL; p = p->next)
            (*freeP)(p->priority);
    }
    if (freeV != NULL) {
        PQNode *p;

        for (p = pqd->head; p != NULL; p = p->next)
            (*freeV)(p->value);
    }
}

/*
 * traverses the list, freeing nodes in the list
 */
static void freeList(PqData *pqd) {
    PQNode *p, *q = NULL;

    for (p = pqd->head; p != NULL; p = q) {
        q = p->next;
        free(p);
    }
}

static void pq_destroy(const PrioQueue *pq) {
    PqData *pqd = (PqData *)pq->self;
    purge(pqd, pqd->freePrio, pqd->freeValue);
    freeList(pqd);
    free(pqd);
    free((void *)pq);
}

static void pq_clear(const PrioQueue *pq) {
    PqData *pqd = (PqData *)pq->self;
    purge(pqd, pqd->freePrio, pqd->freeValue);
    freeList(pqd);
    pqd->head = pqd->tail = NULL;
    pqd->size = 0L;
}

static int pq_insert(const PrioQueue *pq, void *priority, void *value) {
    PqData *pqd = (PqData *)pq->self;
    PQNode *new = (PQNode *)malloc(sizeof(PQNode));
    int status = (new != NULL);
    
    if (status) {
        PQNode *prev = NULL, *next;
        new->next = NULL;
        new->priority = priority;
        new->value = value;
        for (next = pqd->head; next != NULL; prev = next, next = next->next)
            if (pqd->cmp(priority, next->priority) < 0)
                break;
//TODO
/*
 * when we reach this point, the following situations can be true:
 *      prev==NULL, next==NULL: linked list was empty
 *      prev==NULL, next!=NULL: insert new at head
 *      prev!=NULL, next!=NULL: insert new between prev and next
 *      prev!=NULL, next==NULL: insert new at tail
 */
    return status;
}

//TODO
static int pq_min(const PrioQueue *pq, void **value) {
    return status;
}

//TODO
static int pq_removeMin(const PrioQueue *pq, void **priority, void **value) {
    return status;
}

static long pq_size(const PrioQueue *pq) {
    PqData *pqd = (PqData *)pq->self;
    return pqd->size;
}

static int pq_isEmpty(const PrioQueue *pq) {
    PqData *pqd = (PqData *)pq->self;
    return (pqd->size == 0L);
}

/*
 * helper function to generate array of void *'s for toArray and itCreate
 */
static void **genArray(PqData *pqd) {
    void **theArray = NULL;
    if (pqd->size >0L) {
        theArray = (void **)malloc(pqd->size*sizeof(void *));
        if (theArray != NULL) {
            long i = 0L;
            PQNode *p;
            for (p = pqd->head; p != NULL; p = p->next)
                theArray[i++] = p->value;
        }
    }
    return theArray;
}

static void **pq_toArray(const PrioQueue *pq, long *len) {
    PqData *pqd = (PqData *)pq->self;
    void **tmp = genArray(pqd);
    if (tmp != NULL)
        *len = pqd->size;
    return tmp;
}

static const Iterator *pq_itCreate(const PrioQueue *pq) {
    PqData *pqd =(PqData *)pq->self;
    const Iterator *it = NULL;
    void **tmp = genArray(pqd);
    if (tmp != NULL) {
        it = Iterator_create(pqd->size, tmp);
        if (it == NULL)
            free(tmp);
    }
    return it;
}

static const PrioQueue *pq_create(const PrioQueue *pq);

static PrioQueue template = {
    NULL, pq_create, pq_destroy, pq_clear, pq_insert, pq_min, pq_removeMin,
    pq_size, pq_isEmpty, pq_toArray, pq_itCreate
};

static void doNothing(__attribute__((unused)) void *e) {
}

/*
 * helper function to create a new Priority Queue dispatch table
 */
static const PrioQueue *newPrioQueue(int (*cmp)(void*,void*),
                                     void (*freeP)(void*),
                                     void (*freeV)(void*)) {
	//TODO
    return pq;
}

static const PrioQueue *pq_create(const PrioQueue *pq) {
    PqData *pqd = (PqData *)pq->self;

    return newPrioQueue(pqd->cmp, pqd->freePrio, pqd->freeValue);
}

const PrioQueue *LListPrioQueue(int (*cmp)(void *p1, void *p2),
                                void (*freePrio)(void *prio),
                                void (*freeValue)(void *value)) {
    return newPrioQueue(cmp, freePrio, freeValue);
}

const PrioQueue *PrioQueue_create(int (*cmp)(void *p1, void *p2),
                                  void (*freePrio)(void *prio),
                                  void (*freeValue)(void *value)) {
    return newPrioQueue(cmp, freePrio, freeValue);
}
