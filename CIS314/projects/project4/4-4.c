/*
Author: Luke Vandecasteele
Date: 2/5/2021 Last Modified: 2/5/2021
Credits: None
Description: Optimizing array lookups using knowledge about assembly.
Notes:
      1.TODO
   */

#include <stdio.h>

//optimized assembly code for an array transpose
/*
.L10:
movq (%rax), %rcx
movq (%rdx), %rsi
movq %rsi, (%rax)
movq %rcx, (%rdx)
addq $8, %rax
addq $32, %rdx
cmpq %r9, %rax
jne .L10
    */

#define N 4
typedef long array_t[N][N];

void transpose(array_t a){
  for(long i = 0; i < N; ++i){
    long *rp = &a[i][0];
    long *cp = &a[0][i];
    while(rp != cp){
	    long t1 = *rp;
	    long t2 = *cp;
	    *rp = t2;
	    *cp = t1;
	    rp++;
	    cp += N;
    }
  }
}


int main(){
  array_t list = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
  transpose(list);
  for (long i = 0; i < N; ++i) {
    for (long j = 0; j < N; ++j) {
      printf("%ld ", list[i][j]);
    }
    printf("\n");
 }
  return 0;
}
