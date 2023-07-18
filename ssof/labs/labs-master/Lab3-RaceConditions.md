# Race Conditions' Lab

The goal for this lab is to learn the basics of Race Conditions attacks.

## What are Race Conditions

Race Conditions are vulnerabilities that may exist in any application that assumes some sort of _atomicity_ in its actions.

For example whenever 2 entities access concurrently the same object there could be a _violation of the assumption of atomicity_ and during that period, also called the _window of vulnerability_ or _window of opportunity_ some undesired event may occur.

The vulnerability is almost always due to a problem of concurrency/lack of proper synchronization between a target and a malicious process(es); or between several processes/threads of the target.

The attacker races to _break the assumption_ of atomicity during the window of vulnerability.

Remember, __you must be in the IST VPN__ in order to be able to play these challenges.

## Real and Effective user-ids

Before we start with our challenges, you must understand the difference between _real user-id_ and _effective user-id_. For that, we have two examples.

### Example 1

Consider the following example

```C
// https://unix.stackexchange.com/questions/166817/using-the-setuid-bit-properly

#define _POSIX_C_SOURCE 200112L // Needed with glibc (e.g., linux).
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void report (uid_t real) {
    printf ("Real UID: %d Effective UID: %d\n",
        real,
        geteuid()
    );
}

int main (void) {
    uid_t real = getuid();
    report(real);
    seteuid(real);
    report(real);
    return 0;
}
```

1. Compile it and run as a regular user

    ```bash
    gcc testuid.c -o testuid
    ./testuid
    ```

2. Change now the setuid bit of your program so that it runs as `root`.

    ```bash
    sudo chown root testuid
    sudo chmod u+s testuid
    ./testuid
    ```

3. Can you see the differences?

### Example 2

Consider now the following example

```C
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
```

1. Create a text file that you own and compile and run the program as a regular user

    ```bash
    echo "this is a test message" > filetest.txt
    gcc access.c -o access
    ./access filetest.txt
    ./access /etc/passwd
    ./access /etc/shadow
    ```

2. Change now the setuid bit of your program so that it runs as `root` and run it again with the same files

    ```bash
    sudo chown root access
    sudo chmod u+s access
    ./access filetest.txt
    ./access /etc/passwd
    ./access /etc/shadow
    ```

3. Can you see the differences? Do you notice any differences and in particular what checks does the `access` function perform? And `fopen`?

## Problem 1 - A traditional Race - Challenge `I challenge you for a race`

1. First, you should connect to the machine via ssh.

    ```bash
    ssh username@<server> -p <port>
    ```

    __username:passwd__ are available in the scoreboard at the end of Menu _Settings_

2. Look at the folder `/challenge` and inspect the files that exist in there, in particular their permissions. (`ls -al`)

3. The only place with write permissions is `/tmp`. You can use the `/tmp` folder to write your files, but you can't list the files it contains as you do not have read permissions.

4. Create a directory with a _weird name_ inside `/tmp` so that only you would know and write whatever you need inside it: `/tmp/<your_weird_name>/`

5. Remember
    - this machine is shared with everyone else. Be courteous to others and do not exhaust all the resources of the machine. Also do not forget to kill your processes as soon as you find the flag.
        - `ps aux` returns your running processes.
        - `kill PID` kills the process with process id `PID`.
    - always keep a copy of your files in your machine. `/tmp` folder will be cleaned often and without advance notice so do not expect your folder to be there for a long period.
    - we may reboot this machine without notice. Read 2.

6. Get your flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

## Problem 2 - Race conditions exist everywhere - Challenge `Another jackpot`

This is an example that illustrates that _race conditions_ are more than just changing symbolic links from one place to another.

Look at the source code of this challenge and see what is wrong.

Clearly the (intended) _atomicity_ property of this challenge is broken. Exploit it.

It might be useful to script your solution using Python requests. A sample is [here](code/requests_template.py).

Get your flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

## Problem 3 - Pickles in a seri(al)ous race - Challenge `Pickles in a seri(al)ous race`

This is a tough challenge for hungry students. Look at the source code and Google for problems that might occur when serialization is controlled by user.

Then, just win the race and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

## Assessment

This week the exercises used for assessment are:

- I challenge you for a race (10 points)
- Another jackpot (9 points)
- Pickles in a seri(al)ous race (1 point)

You should submit a writeup on how you solved the challenges. For that, create a folder named `lab3` in the repo assigned to you, and create __one writeup per challenge__ named `name_of_the_challenge.md`.
A sample can be found [here](writeup.md).
