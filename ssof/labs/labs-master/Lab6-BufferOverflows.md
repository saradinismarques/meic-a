# Buffer Overflow Exploitation

For this lab we propose a series of simple exercises `Simple Overflow` to `Super Secure Lottery` (category `Buffer-Overflow`) that were adapted from the [Exploit Exercises Project](https://exploit-exercises.com/) namely the [Protostar Project](https://exploit-exercises.com/protostar/) and from the book ___Hacking, The Art of Exploitation___ by Jon Erickson.

The goal of this session is to analyse and exploit buffer-overflow vulnerabilities.
Buffer-overflow vulnerabilities occur when someone is allowed to write and/or to execute code in areas that one should not, and usually derives from the usage of unsafe functions like `gets`.

Modern OS's and compilers already incorporate some security features that prevent these attacks such as _Canaries_, _Executable space protection (XP)/Data Execution Prevention (DEP)_, _Address Space Layout Randomisation (ASLR)_, and _Position Independent Executable (PIE)_.

1. _Canaries_ (or _Stack Cookies_) are known values that are placed between a buffer and control data on the stack to monitor buffer overflows. When the buffer overflows occur, the first data to be corrupted will be the canary, and a failed verification of the canary data is therefore an alert of an overflow;
2. _Executable space protection (XP)_ prevents certain memory sectors, e.g. the stack, from being executable;
3. _Address Space Layout Randomisation (ASLR)_ is a security feature used to help prevent shell-code from being successful. It does this by randomly offsetting the location of modules and certain in-memory structures; and
4. _PIE_ is a compilation option that makes the binary position independent. This means that in the presence of _ASLR_  the kernel loads the binary and dependencies into a random location of virtual memory each time the program runs.

Combining these protection techniques makes it very difficult to exploit vulnerabilities in applications using shell-code or return-oriented programming (ROP) techniques. In order for our attacks to succeed we'll thus need to disable them. For that we compiled our programs using the following flags (we use here `vuln.c` as the program to be compiled, and `vuln` as the generated binary).

__Disable canaries:__ `gcc vuln.c -o vuln -fno-stack-protector`

__Disable XP:__ `gcc vuln.c -o vuln -z execstack`

__Enable XP:__ `gcc vuln.c -o vuln -z noexecstack`

__Disable PIE:__ `gcc vuln.c -o vuln -no-pie`

ASLR is a security of the feature of the OS. To disable/enable ASLR we do it for the whole system:

__Disable ASLR:__ `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`

__Enable ASLR:__ `echo 2 | sudo tee /proc/sys/kernel/randomize_va_space`

To interact with the server you can use the following snippet: [netcat_template.py](code/netcat_template.py)

## Setup

Start by disabling ASLR in your VM as we need it for all our exercises.

__If you are working on a VM other than the one we provided you, make sure you also have the 32-bit libraries installed__

    sudo dpkg --add-architecture i386 &&
    sudo apt-get update &&
    sudo dpkg --configure -a &&
    sudo apt-get install libseccomp-dev:i386 seccomp:i386 libc6-dev-i386

Also, install some graphical plugin gor GDB. `PEDA` and `pwndbg` are 2 good ones.

- [PEDA - Python Exploit Development Assistance for GDB](https://github.com/longld/peda)
- [pwndbg](https://github.com/pwndbg/pwndbg)

Finally you may want to recall some GDB Basics [here](GDB.md).

---

## Task 1 -- Exercises with No Protection

### 1. Simple Overflow

This challenge is running at: see challenge _Simple Overflow_ in the scoreboard.

Let us start with program `simple.c`. The goal of this attack is to print the message `YOU WIN!!!` in the screen. How can we do it?

- Recall how variables are stored in the stack; can variable `buffer` interfere with variable `control`?
- You might want to use GDB to see where `buffer` and `control` are stored in memory and how many bytes they are apart.
- Do not know how to use GDB? A quick GDB-101 with a list of basic GDB commands can be found [here](GDB.md).

This file was compiled with no canaries and `-no-pie`.

### 2. Match an Exact Value

Now that you know how to overflow a buffer, can you do it with an exact value? `match.c` file was compiled with no-canaries and `-no-pie`. The goal of this attack is to print the `Congratulations` message in the screen. Can you do it?

- Recall that `0x61626364` is the string `abcd`;
- Are you getting `0xWWXXYYZZ` instead of `0xZZYYXXWW`? Have you heard of `little-endian` and `big-endian`?

This challenge is running at: see challenge _Match an Exact Value_ in the scoreboard.

### 3. Calling Functions

Ok, you already know how to overflow a buffer in a controlled way and change variables to an exact value. But can you call a function that is not called anywhere in our code?  
File `functions.c` was compiled with no-canaries and `-no-pie`. The goal of this attack is to call function `win` and print the `Congratulations` message on the screen. Can you do it?

- Recall that the name of a function in C is the address where this function is written in the memory;
- Can `fp` be `win`?
- To perform this attack you may need to input chars that are non-printable. In the end of this document you have some suggestions on how to do it.

This challenge is running at: see challenge _Calling Functions_ in the scoreboard.

### 4. Return Address

You now know everything about the stack and how to change its values, change the functions that are called and so on.
But can you call a function _even if NO function is called_ anywhere in our code?

File `return.c` was compiled with no-canaries and `-no-pie`. The goal of this attack is to call function `win` and print the `Congratulations` message in the screen. Can you do it?

- Recall that the name of a function in C is the address where this function is written in the memory;
- Is it true that no function is called in our program? How can you call `win`? Recall how the stack is organised and what values are stored in the stack.

This challenge is running at: see challenge _Return Address_ in the scoreboard.

### 5. Super Secure System

The goal of this attack is to gain access to the system without introducing the correct password, i.e., the flag. Can you do it?
Elaborate on Exercise 4.

File `check.c` was compiled with no-canaries and `-no-pie`.

This challenge is running at: see challenge _Super Secure System_ in the scoreboard.

### 6. Super Secure Lottery

You will never be able to succeed in this challenge. You have to guess a completely random lottery value. Do not even try.

File `lottery.c` was compiled with canaries, `-no-pie`, and does not allow execution in the stack (XP enabled).

Canaries are in place to protect us and prevent buffer overflows. Are you sure?

This challenge is running at: see challenge _Super Secure Lottery_ in the scoreboard.

---

## Assessment

This week the exercises used for assessment are:

- Simple Overflow (4 points)
- Match an Exact Value (4 points)
- Calling Functions (4 points)
- Return Address (4 points)
- Super Secure System (2 points)
- Super Secure Lottery (2 points)

You should submit a writeup on how you solved the challenges. For that, create a folder named `lab6` in the repo assigned to you, and create __one writeup per challenge__ named `name_of_the_challenge.md`.
A sample can be found [here](writeup.md).

---

## Extras - Strings with non-printable chars

You may need to input chars that are non-printable to perform some of these attacks.
If you do not want to script it with `pwntools` (which we strongly encourage you to learn how to do), the easier way to do it is to write such input string to a file, and then use this file as input to the program. For this, do the following:

`python3 -c 'import sys; sys.stdout.buffer.write(bytes1 + bytes2 + ... + bytesn)' > input-file.txt`

or

`python -c 'print(string1 + string2 + ... + stringn)' > input-file.txt`

and afterwards run as

`./program < input-file.txt`

_Example:_

`python3 -c 'import sys; sys.stdout.buffer.write(b"\x48\x31\xc0\x48" + b"\x90" * 30 + b"\x7f\x00\x00")' > input-exerciseX.txt`

or

`python -c 'print("\x48\x31\xc0\x48" + "\x90" * 30 + "\x7f\x00\x00")' > input-exerciseX.txt`

`./file < input-exerciseX.txt`

You can also use the `printf` (or `echo -e`) command

`printf "\x48\x31\xc0\x48\x90\x7f\x00\x00" > input-exerciseY.txt`

`echo -e "\x48\x31\xc0\x48\x90\x7f\x00\x00" > input-exerciseY.txt`

---

## Extras - Some `pwntools` commands

- `from pwn import *` --- load `pwntools` library.

- `p32(address)` --- writes address `0xAABBCCDD` as a string in little-endian `DDCCBBAA`.

- `elf = ELF('./bin')` --- reads ELF binary `bin`

- `elf.symbols['fn']` --- returns the address of function `fn` in the binary (previously read to var `elf`)

- `next(elf.search(string))` --- returns the address of the occurrence of `string` in the binary.
