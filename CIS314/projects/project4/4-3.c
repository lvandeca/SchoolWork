/*Author: Luke Vandecasteele
Date: 2/5/2021 Last Modified: 2/6/2021
Credits: None
Description: Commenting stack push and pop operations depending upon if the
             caller or the callee is responsible for the register.
*/

#include <stdio.h>

//============================Push and pop for fact function===================

long fact(long x) {
 if (x <= 1) {
 return 1;
 }
 long px = x;                 //push onto the stack (1)
 long fx = fact(x - 1);
 return px * fx;              //pop the value in px from the stack (2)
}

/* Further description of push and pop calls

   1. The value of x needs to be saved (pushed ontto the stack) as px by the 
      caller since the value in x needs to be used after another function call.
      In this case, the next function call is the recursion that occurs on the
      following line.
   2. After the recursive call comes back, we will use the returned value (fx) 
      and multiply it by the caller saved value (px) before the recusive call.
      Thus, a push call will be made to retrive px, which is then used in the 
      return statement of the function.
  */

//=================================Main========================================

int main(){
  //testing fact() funtion

  printf("%ld\n", fact(3));
  printf("%ld\n", fact(5));
  printf("%ld\n", fact(2));
  printf("%ld\n", fact(4));
}
