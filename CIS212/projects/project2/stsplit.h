#ifndef _STSPLIT_H_
#define _STSPLIT_H_
/*
 * returns an array of character pointers, one to each word in 'lin'
 * a sentinel pointer of NULL terminates the list
 *
 * the array ofpointers has been allocatied from the heap, and must
 * be returned to the heap by calling stfree() when done with it
 */
char **stsplit(char *line);

/*
 * free the heap-allocated memory returned by stsplit90
 */
void stfree(char **words);

#endif /* _STSPLIT_H_ */

