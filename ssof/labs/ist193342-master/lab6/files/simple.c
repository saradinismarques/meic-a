#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include "general.h"

int main() {
  init();
  int test;
  char buffer[128];

  printf("You win this game if you change variable test to a value different from 0.\n");

  test = 0;
  gets(buffer);

  if(test != 0) {
      printf("YOU WIN!\n");
      printf("Flag: %s\n", getflag());
  } else {
      printf("Try again...\n");
  }
}
