# Challenge `PwnTools Sockets` writeup

- Vulnerability: Bruteforce attack
- Where: `/finish/` endpoint
- Impact: If we get the current number to match the target we can input the word *FINISH* and get the flag

## Steps to reproduce

1. In an infinite loop stablish a session to the remote server with the specified port
2. With the help of Pwntools functions we get the target value from the text received
3. Enter in another infinite loop that gets the current number
4. If the current number is bigger than the target we exit the inner loop and make another connection to the remote server to get a new target
5. If the current number is smaller than the target we continue increasing the current number
6. If the current number is the same as the target we send the input *FINISH* and get the flag

This was done using Pwntools [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab2/pwntools_sockets.py).



