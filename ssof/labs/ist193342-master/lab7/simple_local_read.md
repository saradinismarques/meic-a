# Challenge `Simple Local Read` writeup

- Vulnerability: Format Strings Vulnerability
- Where: function `printf()`
- Impact: Since `printf(str)` is improperly used and the format string str is controlled by us, we can read arbitrary memory content, write to arbitrary memory content, and hijack the execution control flow.


## Steps to reproduce

1. Using GDB, we can put a breakpoint after `get_flag()` is called and print the *secret_value* address:

(gdb) p secret_value

$1 = 0x804d1a0 

2. If we send as input multiple `%p`, we understand the *secret_value* is on the seventh position in the stack:

0x804c000 0xffffcfe8 0x804930a 0x804c000 0x804c000 0xf7fad000 0x804d1a0 (nil) 0x804c000

3. We want the content of the *secret_value* so we use `%s` seven times (`%s.%s.%s.%s.%s.%s.%s.`) instead and we are able to get the flag

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab7/simple_local_read.py)
