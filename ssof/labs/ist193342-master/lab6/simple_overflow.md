# Challenge `Simple Overflow` writeup

- Vulnerability: Buffer Overflow
- Where: function `gets()`
- Impact: This function doesn't do any kind of check while getting bytes from *stdin* so it let's you write in memory more characters than what was allocated for the *buffer* which will overwrite the variable that was declared before it, in this case *test*

## Steps to reproduce

1. First we can use GDB to see where *buffer* and *test* are stored in memmory and how many bytes they are apart. This can be done by doing a breakpoint after the variables are declared and then printing their addresses:

(gdb) p &test 
$1 = (int *) 0xffffcebc
(gdb) p &buffer 
$2 = (char (*)[128]) 0xffffce3c
(gdb) x/100x $sp -> shows stack to better understand where the variables are in memory

2. These two variables are 128 bytes apart as expected so to overwrite *test* we only need to write 128 characters (e.g. 'A') that will be stored in *buffer* and then anything different from 0 (e.g. 'BBBB') that will overwrite what's in *test*

3. We can do this using python and redirect the output to where the challenge is running like this:

python3 -c 'print("A"*128+"BBBB")' | nc mustard.stt.rnl.tecnico.ulisboa.pt 22151

4. This way *test* will be 'BBBB' which is different from 0 so we will enter the *If* statement where the flag will be printed for us


