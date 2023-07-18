from pwn import *

SERVER = ""
PORT = 6660

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

### run a local process
# s = process('./my_program', shell=True)

### interact with it

# s.recvall()
# s.recvuntil(b'Message : ')
# s.recvline()

# s.send(msg + b'\n')
# s.sendline(msg)

# s.interactive()
