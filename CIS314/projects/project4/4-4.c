/*
Author: Luke Vandecasteele
Date: 2/5/2021 Last Modified: 2/5/2021
Credits: None
Description: Optimizing array lookups using knowledge about assembly.
Notes:
      1.TODO
   */

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


