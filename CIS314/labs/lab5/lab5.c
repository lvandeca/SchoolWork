#include <stdio.h>

int sum(long *a, long size){
  long result = 0;
  for(long i = size - 1; i != 0; --i){
    result += a[i];
  }
  return result;
}


int main(){
  long a[3] = {1, 2, 3};
  int x = sum(a, 3);
  printf("%d\n", x);
}







 // movq $0, %rax         //long result = 0
 // subq $1, %rsi         //long i = size - 1 
//.FORSTART:
  //cmpq $-1, %rsi        //i != 0
  //je.FOREND

  //constanst(base, index, mul) -> constant + base + index*mul
  //addq (%rdi, %rsi, 8), %rax      //result += a[i]
  //subq $1, %rsi

  //jmp .FORSTART
//.FOREND:
  //ret
