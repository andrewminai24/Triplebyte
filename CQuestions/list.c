
#include <stdio.h>

int i;

void list(){
  for(int i = 0; i < 10; i++){
    int x = i;
    printf("%i",x);
  }
}
int main(void) {
  list();
  return 0;
}
