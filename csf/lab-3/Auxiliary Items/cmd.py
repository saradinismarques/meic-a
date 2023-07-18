import urllib.request
import urllib.parse
import http.client
import subprocess
import sys
import base64
import os
from Crypto import Random
from Crypto.Cipher import AES
import hashlib

password = "Fj39@vF4@54&8dE@!)(*^+-pL;'dK3J2"
private_key = hashlib.sha256(password.encode("utf-8")).digest()

def decrypt(enc) -> bytes:
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return cipher.decrypt(enc[16:])

def cmd(data):
    return str(decrypt(data), 'utf-8')

def file(data):
    with open("out", "wb") as f:
        result = decrypt(data)
        f.write(result)
        f.close()

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        data = f.read()
        parsed = urllib.parse.parse_qs(data)
        if "cmd" in parsed:
            print(cmd(parsed["cmd"][0]))
        else:
            file(parsed["file"][0])
