# Challenge `Match an Exact Value` writeup

- Vulnerability: Buffer Overflow
- Where: function `gets()`
- Impact: This function doesn't do any kind of check while getting bytes from *stdin* so it let's you write in memory more characters than what was allocated for the *buffer* which will overwrite the variable that was declared before it, in this case *test*

## Steps to reproduce

1. This challenge is similar to `Simple Overflow` only this time the *buffer* has size 64 so it will be separated from *test* 64 bytes and we want *test* to have the exact value of `0x61626364`

2. So we want to send 64 'A's and then the value `0x61626364` which we will write as `\x64\x63\x62\x61` in print in python due to the endianness the characters are represented in

3. This can be done with the following command:

python3 -c 'print("A"*64+"\x64\x63\x62\x61")' | nc mustard.stt.rnl.tecnico.ulisboa.pt 22152

4. This way *test* will be `0x61626364` so we will enter in the *If* statement where the flag will be printed for us

