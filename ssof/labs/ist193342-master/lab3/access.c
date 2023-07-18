#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[]){
    FILE* f;

    if(!access(argv[1], R_OK)) // 0 if the user has read privilege
        printf("OK  access READ to file %s\n", argv[1]);
    else
        printf("NOK access READ to file %s\n", argv[1]);

    if(!access(argv[1], W_OK)) // 0 if the user has write privilege
        printf("OK  access WRITE to file %s\n", argv[1]);
    else
        printf("NOK access WRITE to file %s\n", argv[1]);

    f = fopen(argv[1], "r");
    if (f == NULL)
        printf("NOK open for READING from file %s\n", argv[1]);
    else
        printf("OK  open for READING from file %s\n", argv[1]);

    f = fopen(argv[1], "a");
    if (f == NULL)
        printf("NOK open for WRITING to file %s\n", argv[1]);
    else
        printf("OK  open for WRITING to file %s\n", argv[1]);
}
