import requests
import re

s = requests.Session()
req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22051')

for current_number in range(0,1000):
    req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22051/number/'+str(current_number))
    
    print(current_number)
    if("Nope" in req.text):
        current_number += 1
    else:
        print(req.text)
        break
    
