# Challenge `Python requests Again` writeup

- Vulnerability: Bruteforce attack
- Where: `/finish/` endpoint
- Impact: If we get the current number to match the target we can access `/finish/` and get the flag like the previous exercise but supposedly we only have one try

## Steps to reproduce

1. In an infinite loop stablish a session and do a request in that URL to find the target wich we are aiming for and the cookie **user**
2. Do another request but this time setting the cookies **remaining_tries** to a big number and the cookie **user** to the one we get previously
3. The rest is done like the previous exercise: enter in a infinite while loop to increase the current number by doing a request to `/more/` 
4. If the current number is the same as the target we can access `/finish/` and get the flag
5. Else we continue increasing or decreasing (this time however we can get a negative number so the current number can decrease)

This was done using python requests [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab2/python_requests_again.py).

