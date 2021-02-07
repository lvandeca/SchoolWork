/* Author: Luke Vandecasteele
Date: 2/4/2021 Last Modified: 2/6/2021
Credits: None
Description: Simple problem solving between assembly and C code
*/

#include <stdio.h>

//========================Assembly and loop function===========================

//loop:
//  movq %rsi, %rcx         //put b into the increment register
//  movl $1, %eax           //store 1
//  movl $0, %edx           //store 0
//.L2:
//  testq %rax, %rax        //check that mask is not 0
//  je .L4
//  movq %rax, %r8          //move mask out of return register
//  andq %rdi, %r8          //(mask & a) store in mask
//  orq %r8, %rdx           //or result and mask 
//  salq %cl, %rax          //left shift mask by b
//  jmp .L2
//.L4:
//  movq %rdx, %rax
//  ret


long loop(long a, long b){
  long result = 0;
  for (long mask = 1; mask != 0; mask <<= b){
    result |= (mask & a);
  }
  return result;
}

//===================================Main======================================

int main(){
  //test runs for loop()
  printf("%ld\n", loop(1, 5));      // = 1
  printf("%ld\n", loop(2, 4));      // = 0
  printf("%ld\n", loop(3, 3));      // = 1
  printf("%ld\n", loop(4, 2));      // = 4
  printf("%ld\n", loop(5, 1));      // = 5

  return 0;
}
