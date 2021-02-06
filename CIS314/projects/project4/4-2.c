/* Author: Luke Vandecasteele
Date: 1/5/2021 Last Modified: 2/5/2021
Credits: None
Description: using "goto" and labels plus writing in assembly
Notes:
       1. TODO
*/


#include <stdio.h>

//impelentation of sum() function from q2 using a goto label


/*
int sum(int from, int to){
  int result = 0;

  L1:
    result += from;
    ++from;
  if(from <= to){
    goto L1;
  }
  return result;
}
*/

long sum(long from, long to) {
// Declare and initialize result var – *do not modify*.
long result = 0;

// Ensure that argument *from* is in %rdi,
// argument *to* is in %rsi, *result* is in %rax - *do not
// modify*.
__asm__ ("movq %0, %%rdi # from in rdi;" :: "r" ( from ));
__asm__ ("movq %0, %%rsi # to in rsi;" :: "r" ( to ));
__asm__ ("movq %0, %%rax # result in rax;" :: "r" ( result ));

// Your x86-64 code goes below - comment each instruction...
__asm__(
// TODO - Replace the two lines below with add, compare,
// jump instructions, labels, etc as necessary to implement
// the loop.
".L2:;"             // # label loop
"addq %rdi, %rax;"  // # result += from
"addq $1, %rdi;"    // # increment from (++from)
"cmp %rsi, %rdi;"   // # if statement to set flags
"jle .L2;"          // # jump if from is <= to
);

// Ensure that *result* is in %rax for return - *do not modify*.
__asm__ ("movq %%rax, %0 #result in rax;" : "=r" ( result ));
return result;
}

int main(){
  printf("%ld\n", sum(1L,6L));     // 21
  printf("%ld\n", sum(3L,5L));     // 12
  printf("%ld\n", sum(5L,3L));     // 5
  return 0;
}
