# Challenge `Python requests` writeup

- Vulnerability: Bruteforce attack
- Where: `/finish/` endpoint
- Impact: If we get the current number to match the target we can access `/finish/` and get the flag

## Steps to reproduce

1. In an infinite loop stablish a session in that URL and do a request to find the target wich we are aiming for
2. Enter in a infinite while loop to increase the current number by doing a request to `/more/` 
3. If the current number is bigger than the target we exit the inner loop and stablish a new session to get a new target
4. If the current number is smaller than the target we continue increasing the current number
5. If the current number is the same as the target we can access `/finish/` and get the flag

This was done using python requests [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab2/python_requests.py).

