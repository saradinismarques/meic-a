# Lab 2 - Interacting with a Remote Server

The goal of this class is to learn how to interact with a remote server using the `requests` and `pwntools` Python modules.  

Don't forget that in order to access our servers you need to be either:

- Working on an RNL Lab computer,
- Connected to Técnico [VPN](README.md#2-connect-to-t%C3%A9cnico-vpn) on the VM, or
- Connected to Técnico [VPN](README.md#2-connect-to-t%C3%A9cnico-vpn) on the host system.

If you have not done it yet, please follow the instructions on [README.md](README.md) and [Introduction](Introduction.md) in order to

1. [Download and set up our Virtual Machine](README.md#1-virtual-machine)
2. [Connect to Técnico VPN](README.md#2-connect-to-t%C3%A9cnico-vpn)
3. [Register yourself in our scoreboard](README.md#3-scoreboard)

## 1. Learn how to use Python Requests - Challenge `Python requests`

During this course you will need to interact with HTTP servers and a good way to do it is using the `requests` Python module.

This module is already installed in our VMs, but you can install it on your system running in the terminal:

    pip install requests (or pip3 install requests)

To practice we have prepared challenge `Python requests` that is available in the scoreboard. Follow the given HTTP URL to access the challenge.

The goal is simple: you are given a `target` number and you should access the endpoint `/more` to get more numbers (randomly positive or negative) until the sum of all numbers received so far adds up to `target`.  
Once you reach the target value, you should access the endpoint `/finish` to get the flag.

Notice that

- a) the start of the game is the endpoint `hello`.
- b) the state is preserved using cookies, so don't forget to make new requests with the cookies that were received in the previous response.

Once you get the flag, submit it to your scoreboard account to score points.

__Hints:__

- Are you being redirected to `/hello` when you request `/more`? See b) above.

__Note: while possible, the point of this exercise is NOT to get the flag manually using a browser, but to automate the process using a Python script! Don't squander this chance to practice!__

You can find [here](./code/requests_template.py) a template on how to use module `requests`.

You can find [here](https://requests.readthedocs.io/en/latest/) documentation for `requests`.

## 2. Learn how to play with cookies - Challenge `Python requests Again`

(Note: unlocked after completing `Python requests`)

The challenge `Python requests Again` is much like the previous one, but now you are only give one chance to reach `target`. Are you lucky enough to make it?

## 3. `Secure by Design`

(Note: unlocked after completing `Python requests`)

## 4. Learn how to use sockets with `pwntools` - Challenge `PwnTools Sockets`

During the course you will also need to interact with servers over raw sockets and a good way to do it is using package `pwntools` for Python.

This module is already installed in our VMs, but you can install it on your system running in the terminal:

    pip install pwntools (or pip3 install pwntools)

To practice we have prepared challenge `PwnTools Sockets` that is available in the scoreboard. Follow the given link to access the challenge.

This challenge is the same game as `Python requests` but now over sockets.  
Instead of accessing the endpoint `/more` you should send a line with the characters `MORE`, and instead of accessing the endpoint `/finish`, you should send `FINISH`.

You can find [here](./code/netcat_template.py) a template on how to connect to a remote server over sockets using module `pwntools`.

Some additional resources:

- [pwntools GitHub page](https://github.com/Gallopsled/pwntools#readme)
- [pwntools docs](https://docs.pwntools.com/en/latest/)
- [pwntools tutorial](https://github.com/Gallopsled/pwntools-tutorial#readme)

## Assessment

This week the exercises used for assessment are:

- Guess a BIG Number
- Python requests
- Python requests Again
- PwnTools Sockets
- Secure by Design

You should submit a writeup on how you solved the challenges. For that, create a folder named `lab2` in the repo assigned to you, and create __one writeup per challenge__ named `name_of_the_challenge.md`.
A sample can be found [here](writeup.md).
