/*Author: Luke Vandecasteele
 *Date: 1/28/2021 Last Modified: 1/29/2021
 *Description: Representation and display of basic integer
 *             array.
 *Credits: Bubble sort algorithm for function 
 *         void printIntArray(struct IntArray) from 
 *         https://www.geeksforgeeks.org/c-program-for-bubble-sort/
 *         Swap function copied from Week 4 class slides.
 *Notes:
 *      1. Created for CIS 313 at University of Oregon Assignment 3
 *         problem 1.
 */


#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct IntArray{
  /*Basic integer array struct*/

  int length;
  int *dataPtr;
};


struct IntArray* mallocIntArray(int length){
  /*Instance creation of a struct IntArray* */

  struct IntArray *arrayPtr = (struct IntArray*)malloc(sizeof(struct IntArray*));

  if(arrayPtr != NULL){                     //arrayPtr malloc is successful

    //memory allocated is size of the dataPtr in struct IntArray*, times input length
    int *dataPtr = (int *)malloc(sizeof(int *) * length);

    if(dataPtr != NULL){                    //dataPtr malloc is successful 
      arrayPtr->length = length;            //store input length in arrayPtr
      arrayPtr->dataPtr = dataPtr;          //store malloced int* arrayPtr 

    } else {                                //int* malloc failed then:
      free(dataPtr);                        //free memory for arrayPtr
    }
  }

  return arrayPtr;                          //return instance creation
}


void freeIntArray(struct IntArray *arrayPtr){
  /*Returns memory allocated on the heap for struct IntArray* */

  free(arrayPtr->dataPtr);                  //first free int *dataPtr
  free(arrayPtr);                           //free instance
}


void readIntArray(struct IntArray *array){
  /*Function prompting user to fill struct IntArray* */

  char line[20];
	char *result = NULL;
  int length = 0;
  
  while(length < array->length){            //ask for input until array full  
	  printf("Enter int: ");
	  result = fgets(line, 20, stdin);        //get input from standard input

	  if(result == NULL){                     //no input is given
		  printf("Invalid input.\n");
      continue;
	  } 

	  long count = 0;
	  char *endptr = NULL;
	  count = strtol(line, &endptr, 10);

	  if(line == endptr || count < 1) {       //input is not a positive integer
		  printf("Invalid input.\n");
      continue;
	  }

    array->dataPtr[length++] = (int)count;  //valid input: add to array,
  }                                         //increment current length counter
}


void swap(int *xp, int *yp){
  /*Basic swap function. Called by sortIntArray
   * for Bubble sort implementation. Credited 
   * in header.*/

  int t0 = *xp;
  int t1 = *yp;
  *xp = t1;
  *yp = t0;
}


void sortIntArray(struct IntArray *array){
  /*Bubble sort implementation for struct IntArray* 
   * Credited in header. Adapted for struct IntArray*/

  int i, j; 
  int len = array->length;
  for (i = 0; i < len - 1; i++){       
  
    for (j = 0; j < len-i-1; j++){          //Last i elements are already in place           

      if (array->dataPtr[j] > array->dataPtr[j+1]){
        swap(&array->dataPtr[j], &array->dataPtr[j+1]);    //call swap()
    
     }  
    }
  }
}


void printIntArray(struct IntArray *array){
  /*Function to print contents of struct IntArray* */

  int i;
  int l = array->length;                           //get length from IntArray*

  for(i = 0; i < l; i++){                          //iterate through array->dataPtr
    char *prefix = (i == 0) ? "[" : "";            //prefix is '[' for first element
    char *suffix = (i == (l - 1)) ? "]" : ", ";    //suffix is ']' for last element,
                                                   //', ' for middle elements

    printf("%s%d%s", prefix, (array->dataPtr[i]), suffix);
  }

  printf("\n");
}


int main() {
 /*Driver function for user to create a struct IntArray*
  * instance, then use all functins for an IntArray* 
  * printing a sorted output. Calls all IntArray
  * functions above.
  */

  char line[20];
	char *result = NULL;
  int input = 1;
	long count = 0;
  
  while(input){                             //prompt user until vaild input
	  printf("Enter length: ");               //is given for array length
	  result = fgets(line, 20, stdin);

	  if(result == NULL){                     //no input detected
		  printf("Invalid input.\n");
      continue;
	  } 

	  char *endptr = NULL;
	  count = strtol(line, &endptr, 10);

	  if(line == endptr || count < 1) {       //input is not a positive integer
		  printf("Invalid input.\n");
      continue;
	  }
    
    input = 0;
  }

  //Valid input input is given. Create instance of struct IntArray* 
  struct IntArray *arrayPtr = mallocIntArray((int)count);

  readIntArray(arrayPtr);                   //prompt user to fill arrayPtr
  sortIntArray(arrayPtr);                   //sort users array
  printIntArray(arrayPtr);                  //print sorted array to stdout
  freeIntArray(arrayPtr);                   //return memory allocated

  return 0;
} 
