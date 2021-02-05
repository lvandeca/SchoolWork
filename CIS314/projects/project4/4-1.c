/* Author: Luke Vandecasteele
Date: 2/4/2021 Last Modified: 2/4/2021
Credits: None
Description: Simple problem solving between assembly and C code
*/

#include <stdio.h>


//loop:
//  movq %rsi, %rcx         #
//  movl $1, %eax
//  movl $0, %edx
//.L2:
//  testq %rax, %rax
//  je .L4
//  movq %rax, %r8
//  andq %rdi, %r8
//  orq %r8, %rdx
//  salq %cl, %rax
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


int main(){
  //test runs for loop()
  printf("%ld\n", loop(1, 5));      // = 1
  printf("%ld\n", loop(2, 4));      // = 0
  printf("%ld\n", loop(3, 3));      // = 1
  printf("%ld\n", loop(4, 2));      // = 4
  printf("%ld\n", loop(5, 1));      // = 5

  return 0;
}
