# Challenge `Write Big Numbers` writeup

- Vulnerability: Format Strings Vulnerability
- Where: function `printf()`
- Impact: Since `printf(str)` is improperly used and the format string str is controlled by us, we can read arbitrary memory content, write to arbitrary memory content, and hijack the execution control flow.


## Steps to reproduce

1. This is similar to the previous challenge but now we want *target* to be exactly 0x0f5f1aa9

2. Both address and position in the stack of *target* variable are the same so we will have to send first that address, then 6 `%x` and `%n` that will write to *target*

3. We want to write 0x0f5f1aa9=257890985 characters. One way to do this is sending the address (4 characters), 5 times `%08x ` (5\*9=45 characters) and `%257890935x ` (257890936 characters). The total number of characters will be 4+45+257890936=257890985=0x0f5f1aa9 so this value will be written to *target* and the flag will be printed

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab7/write_big_number.py)



