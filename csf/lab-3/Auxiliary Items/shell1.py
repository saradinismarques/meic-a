#!/usr/bin/python
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
enc = base64.b64decode(sys.argv[1])
iv = enc[:16]
cipher = AES.new(private_key, AES.MODE_CFB, iv)
print(cipher.decrypt(enc[16:]))
