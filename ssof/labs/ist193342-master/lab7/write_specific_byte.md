# Challenge `Write Specific Byte` writeup

- Vulnerability: Format Strings Vulnerability
- Where: function `printf()`
- Impact: Since `printf(str)` is improperly used and the format string str is controlled by us, we can read arbitrary memory content, write to arbitrary memory content, and hijack the execution control flow.


## Steps to reproduce

1. This is similar to the previous challenge but now we want *target* to be at least 0x01000000 so the condition `target & 0xff000000` is evaluated to True

2. This time the *target*'s address is 0x0804a044 but is on the same position in stack:

objdump -t bin | grep target

0804a048 g     O .bss   00000004              target_after

0804a044 g     O .bss   00000004              target

0804a040 g     O .bss   00000004              target_before

3. We want to write 0x01000000=16777216 characters. One way to do this is sending the address (4 characters), 5 times `%08x` (5\*8=40 characters) and `%016777172x` (16777172 characters). The total number of characters will be 4+40+16777172=16777216=0x01000000 so this value will be written to *target* and the flag will be printed

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab7/write_specific_byte.py)

