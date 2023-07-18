# Challenge `Short Local Read` writeup

- Vulnerability: Format Strings Vulnerability
- Where: function `printf()`
- Impact: Since `printf(str)` is improperly used and the format string str is controlled by us, we can read arbitrary memory content, write to arbitrary memory content, and hijack the execution control flow.


## Steps to reproduce

1. This is similar to the previous challenge but we can only pass as input 5 characters

2. The variable *sectre_value* has the same address and is on the same position in the stack as the previous challenge so we have to print the seventh position content in a way that takes less characters

3. This can be done using `%7$s` instead of `%s.%s.%s.%s.%s.%s.%s.`. It will print only the seventh register of the stack immediately after the format string without the need to print the previous ones.

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab7/short_local_read.py)
