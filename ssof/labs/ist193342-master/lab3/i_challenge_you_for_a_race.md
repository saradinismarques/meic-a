# Challenge `I challenge you for a race` writeup

- Vulnerability: Race Conditions
- Where: **access** function
- Impact: We can create a symbolic link to the file `flag` in the `challenge` directory and since we now have permissions to read it we extract the flag

## Steps to reproduce

1. Create a directory in `/tmp` with some weird name (e.g. `/ist193342`) where we can create our script since here we have read and write permissions
2. In the script we create two files that have read and write permissions `normal` and `dummy`
3. In an infinite loop we make a symbolic link from the `dummy` file to the `normal` file
4. Next we run the challenge passing as input the previously created `dummy` file and at the same time we change the symbolic link of the `dummy` file to point to the `flag` file thas has no read permission. Since the **access** function is vulnerable to race condition if we get the timing right we can read the `flag` file using the read permissions that the `normal` file has
5. The output of this concurrent operation is saved in a variable **OUTPUT**
6. If the beginning of the flag - *SSof* - is contained in **OUTPUT** we print it, get the flag and exit the infinite loop

This was done using a bash script [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab3/i_challenge_you_for_a_race.sh).



