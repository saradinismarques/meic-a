# Challenge `Guess a BIG Number` writeup

- Vulnerability: Bruteforce attack
- Where: `/number/<guess>` endpoint
- Impact: If we guess the right number between 0 and 100000 and access `/number/<right number>` we can get the flag

## Steps to reproduce

1. Start guessing with the number 50000 (half of 100000) in a variable called **current_name**. There is also a variable called **gap** with the size of the interval of possible numbers 
2. Enter in an infinite loop trying to guess the number
3. If we get *Higher!* increase the **current_number** by half the current **gap** and reduce the **gap** to half
4. If we get *Lower!* reduce the **current_number** by half the current **gap** and reduce the **gap** to half 
5. If we get the right number we get the flag and exit the loop
 
This was done using python requests [here]().

