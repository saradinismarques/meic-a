#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "general.h"

#define GUESS_SIZE 64
#define LOTTERY_LEN 8

void run_lottery(const char* prize) {
    char guess[LOTTERY_LEN] = {0};

    while (1) {
        printf("What is your guess: ");
        read(0, guess, GUESS_SIZE);

        if (!memcmp(prize, guess, LOTTERY_LEN)) {
            printf("Congratulations! You won the lottery: %s\n", getflag());
        } else {
            puts("Wrong guess. Do you want to play again?");
        }
    }
}

int main() {
    init();
    char lottery[LOTTERY_LEN];

    int fd = open("/dev/urandom", O_RDONLY);
    read(fd, lottery, LOTTERY_LEN);
    close(fd);

    run_lottery(lottery);
}
