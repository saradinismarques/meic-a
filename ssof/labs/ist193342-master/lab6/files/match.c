#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include "general.h"

int main() {
  init();
  int test;
  char buffer[64];

  printf("You win this game if you can change variable test to the value 0x61626364. Have you noticed that the ascii code of 'a' is 0x61?\n");

  test = 0;
  gets(buffer);

  if (test == 0x61626364) {
      printf("Congratulations, you win!!! You correctly got the variable to the right value\n");
      printf("Flag: %s\n", getflag());
  } else {
      printf("Try again, you got 0x%08x, instead of 0x61626364\n", test);
  }
}
