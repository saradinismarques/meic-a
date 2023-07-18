# Challenge `Another jackpot` writeup

- Vulnerability: Race Conditions
- Where: **login** function
- Impact: In the **login** function of the server there is a line (no. 167) where the username can be setted to anything without checking if it exists or the password is correct. Only on line no. 170 this verification is done. To get the flag we have to access the `/jackpot` page with the username setted as *admin* and the flag is printed on the webpage

## Steps to reproduce

1. To explore the race condition vulnerability we can use the **grequests** library to make asynchronous HTTP Requests easily
2. Start by creating a session and do a request to the server
3. In a infinite loop make two requests to the server at the same time. One does a **post** request to the `/login` page inputing to the forms the username *admin* and some random password. The second does a **get** request to the `/jackpot` page. This way we are exploring the race condition vulnerability by trying to get the timing right in setting the username to *admin* and accessing the `/jackpot` page without checking the password before. This is all done in the same session. 
4. The output of this two concurrent requests is saved in a variable **res**
5. If the beginning of the flag - *SSof{* - is contained in **res** we have the flag and can exit the infinite loop

This was done using pyhton requests [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab3/another_jackpot.py).



