#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    char file_to_read[64] = {0};

    printf("Insert filename to read: ");
    fflush(stdout);

    int res = read(STDIN_FILENO, file_to_read, sizeof(file_to_read));
    file_to_read[res-1] = '\x00';

    if(!access(file_to_read, R_OK)) {
        FILE *fd;
        char buffer[2048] = {0};

        puts("Content: \n===========================\n");

        fd = fopen(file_to_read, "r");
        fread(buffer, sizeof(buffer), 1, fd);

        printf("%s\n", buffer);
        puts("===========================");
    } else {
        printf("No permission to read '%s'\n", file_to_read);
    }

    return 0;
}
