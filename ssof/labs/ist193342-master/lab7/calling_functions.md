# Challenge `Calling Functions` writeup

- Vulnerability: Format Strings Vulnerability
- Where: function `printf()`
- Impact: Since `printf(str)` is improperly used and the format string str is controlled by us, we can read arbitrary memory content, write to arbitrary memory content, and hijack the execution control flow.


## Steps to reproduce

1. We start by checking the addresses of the functions `win()` and `exit()`:

\$ objdump -t bin | grep win 

0804849b g     F .text	00000029              win

\$ objdump -R bin | grep exit 

0804a018 R_386_JUMP_SLOT   exit@GLIBC_2.0

2. We want to write 0x0804849b in 0x0804a018 so that when the program is exiting the function `vuln()` it will jump to the function `win()`

3. Since the first 2 bytes of both addresses are the same we can use `%hn` to write only on the 2 least significant bytes to prevent a big output

4. We want to write 0x849b=33947 characters. One way to do this is sending the address (4 characters), 5 times `%08x` (5\*8=40 characters) and `%33903x` (33903 characters). The total number of characters will be 4+40+33903=33947=0x849b so this value will be written on the last 2 bytes of `exit()` function becoming 0x0804849b and program execution will jump to the function `win()` where the flag will printed

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab7/calling_functions.py)



