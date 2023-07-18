from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22055

while(True):
    ### run a remote process
    s = remote(SERVER, PORT, timeout=9999)

    ### interact with it
    s.recvuntil(b'you get to ')
    target = s.recvline(b'.')
    target = int(target[:-2])
    print("Target: " + str(target))

    finished = False
    
    while(True):
        s.recvuntil(b'CURRENT = ')
        current = s.recvline(b'.')
        current = int(current[:-2])
        print("Current: " + str(current))

        if(current > target):
            break
        elif(current == target):
            s.sendline(b'FINISH')
            flag = s.recvall()
            print(flag)
            finished = True
            break
        else:
            s.sendline(b'MORE')

    if(finished):
        break


