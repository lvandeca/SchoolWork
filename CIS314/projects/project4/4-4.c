/*
Author: Luke Vandecasteele
Date: 2/5/2021 Last Modified: 2/6/2021
Credits: None
Description: Optimizing array lookups using knowledge about assembly.
Notes:
      1.Used a while loop in inner loop for function transpose. Could easily
        be done with a for loop where the increment values at the end of 
        while loop move into the for loop.
   */

#include <stdio.h>

//======================Optimized assebly and correspoding C code==============

/* optimized assembly code for an array transpose
.L10:
movq (%rax), %rcx     //store value in t1 from a[i][j]
movq (%rdx), %rsi     //store value in t2 from a[j][i]
movq %rsi, (%rax)     //replace value in a[i][j] with t2
movq %rcx, (%rdx)     //replace value in a[j][i] with t1
addq $8, %rax         //increment to next column in row (or ++i)
addq $32, %rdx        //increment to next row in comlumn (or ++j)
cmpq %r9, %rax        //compare if the row is at the end of the matrix
jne .L10              //this is like j < i comparison in unoptimized code
    */

#define N 4
typedef long array_t[N][N];

void transpose(array_t a){
  //optimised version of a matrix transpose to match the assembly code above
  for(long i = 0; i < N; ++i){
    long *rp = &a[i][0];      //get address of ith row
    long *cp = &a[0][i];      //get adress of ith column
    while(rp != cp){          //continue loop until column and row meet
	    long t1 = *rp;          //temporarily store row value
	    long t2 = *cp;          //temporarily store column value
	    *rp = t2;               //switch the values in row and column
	    *cp = t1;
	    rp++;                   //increase to next column in row
	    cp += N;                //increase to next row in the current column
    }
  }
}

//================================Main=========================================

int main(){
  //quick test for transpose function
  array_t list = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
  transpose(list);
  
  //quick for loop to simply print out the matrix after transpose
  //not meant to be optimized
  for (long i = 0; i < N; ++i) {
    for (long j = 0; j < N; ++j) {
      printf("%ld ", list[i][j]);
    }
    printf("\n");
 }
  return 0;
}
