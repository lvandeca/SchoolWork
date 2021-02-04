/*Author: Luke Vandecasteele
 *Date: 1/29/2021 Last Modified: 1/29/2021
 *Description: Basic arithemtic operation for practicing writing C 
               code from x86-64 assembly code compiled on a 
               ArchLinux machine.
 *Credits: Week 4 class slides
 *Notes:
 *      1. Created for CIS 313 at University of Oregon Assignment 3
 *         problem 2.
 */


#include <stdio.h>

long f(long x, long y, long z){
  /*Function to match x86-64 assembly code*/

                                  //to start, x -> %rdi, y -> %rsi, z -> %rdx
  long answer;                    //return, address is %rax
  z = z + y;                      //addq %rsi, %rdx => stored in %rdx
  x = x * z;                      //imulq %rdx, %rdi => stored in %rdi
  z = z << 63;                    //salq $63, %rdx
  z = z >> 63;                    //sarq $63, %rdx
  answer = x;                     //movq %rdi, %rax, %rdi into return regiser
  answer = answer ^ z;            //xorq %rdx, %rax

  return answer;
}


int main(){
  /*Simple tests to check correct output*/

  long test1 = f(1, 2, 4);        //return 6
  printf("%ld\n", test1);

  long test2 = f(3, 5, 7);        //return 36
  printf("%ld\n", test2);

  long test3 = f(10, 20, 30);     //return 500
  printf("%ld\n", test3);
  
  return 0;
}
