# Challenge `Write to Memory` writeup

- Vulnerability: Format Strings Vulnerability
- Where: function `printf()`
- Impact: Since `printf(str)` is improperly used and the format string str is controlled by us, we can read arbitrary memory content, write to arbitrary memory content, and hijack the execution control flow.


## Steps to reproduce

1. We can start by printing the address of the *target* variable using `objdump`:

\$ objdump -t bin | grep target

0804a040 g     O .bss	00000004              target

2. We want to send as input this address and write to it some value different from 0. This can be done sending something like `"\x40\xa0\x04\x08" + "%x."*20` and changing the number of `%x.` until the *target*'s address is printed last. This happens with 7 `%x.`:

@ffffcfdc 7f ffffd044 80482f8 f7fdc6bd 804825c 804a040 

3. If we modify the last `%x` to `%n` we can write a value to that address. The value written will be the number of characters printed so far

3. This way *target* will be different from 0 and the flag will be printed 

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab7/write_to_memory.py)
