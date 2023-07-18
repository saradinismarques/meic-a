# Challenge `Return Address` writeup

- Vulnerability: Buffer Overflow
- Where: function `gets()`
- Impact: This function doesn't do any kind of check while getting bytes from *stdin* so it let's you write in memory more characters than what was allocated for the *buffer* which will overwrite other parts in memory, in this case the return address of the function `challenge()`

## Steps to reproduce

1. First we can confirm using GDB that in the return of the function `challenge()` what's on the top of the stack is the address of the instruction on `main()` right after `challenge()` is called. This can be done using breakpoints and printing the stack's content. This address is `0x08048791`

2. We can also check how many blocks of memory distance the allocation of the *buffer* with the return address (buffer starts on the first '41' which corresponds to an 'A')

(gdb) x/30x $
0xffffce90:     0xffffcea6      0xf7fb4000      0xffffceb8      0x0804873f
0xffffcea0:     0xf7fb4d20      0x41410000      0x41414141      0x41414141
0xffffceb0:     0x00000000      0x00000000      0xffffcec8      0x08048791
0xffffcec0:     0xf7fe22d0      0xffffcee0      0x00000000      0xf7de6ee5

3. The number of complete blocks between the first '41' and the address `0x08048791` is 5 so we will have to write `5*4 + 2 'A's` (*buffer* starts in the middle of a block). After this many 'A's we can overwrite the address of return with the address of the function `win()`:

(gdb) p win
$3 = {void ()} 0x80486f1 <win>

4. After overwritting the return address when `challenge()` ends the program will jump to the function `win()` where the flag will be printed

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab6/return_address.py)