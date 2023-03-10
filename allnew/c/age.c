#include <stdio.h>

int main() {
  int i;  // 지역변수 i , auto가 생략된 것
  printf("Input your age : ");
  scanf("%d", &i); // adress of i(i의 주소)
  printf("Your age is %d \n", i);

  return 0;
}    // 괄호 안에
