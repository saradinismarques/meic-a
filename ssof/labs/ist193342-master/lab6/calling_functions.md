# Challenge `Calling Functions` writeup

- Vulnerability: Buffer Overflow
- Where: function `gets()`
- Impact: This function doesn't do any kind of check while getting bytes from *stdin* so it let's you write in memory more characters than what was allocated for the *buffer* which will overwrite the variable that was declared before it, in this case the pointer *fp*

## Steps to reproduce

1. We want to overwrite *fp* with the address of the function `win()` so that inside the *If* statement after *printf* when we use the pointer it will jump to that address and call that function

2. To find the address of the function `win()` we can run the program in GDB putting a breakpoint befores it ends and there printing the address like this:

(gdb) p win
$1 = {void ()} 0x80486f1 <win>

3. To overwrite what's in *fp* with this address, the input should be 32 'A's (buffer's size) and then the address of the function

4. After overwritting *fp*, when we use the pointer, the program will jump to the function `win()` where the flag will be printed

This was done in python using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab6/calling_funtions.py)