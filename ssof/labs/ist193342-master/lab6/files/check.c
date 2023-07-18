#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include "general.h"

int check_password(char* password) {
  char buffer[32];

  strcpy(buffer, password);

  if(strcmp(buffer, getflag()) == 0)
    return 1;

  return 0;
}

int main() {
  init();

  char pass[64] = {0};
  // we know how to make this secure. No gets in here.
  read(0, pass, 63);

  if(check_password(pass)){
      printf("Welcome back! Here is the secret flag that you already knew: %s\n", getflag());
  } else {
      printf("Unauthorized user/passwd\n");
  }
}

