#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include "general.h"

void win() {
  printf("Congratulations, you win!!! You successfully changed the code flow\n");
  printf("Flag, %s\n", getflag());
}

void challenge() {
  char buffer[10];
  printf("You win this game if you are able to call the function win.'\n");
  gets(buffer);
}
 
int main() {
  init();
  challenge();
  return 0;
}
