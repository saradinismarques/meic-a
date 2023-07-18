import requests
import re

current_number = 50000
gap = 50000
s = requests.Session()
req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22052')

while(True):
    req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22052/number/'+str(current_number))
    
    print(current_number)
    if("Higher!" in req.text):
        current_number = current_number + gap//2
        gap = gap//2
    elif("Lower!" in req.text):
        current_number = current_number - gap//2
        gap = gap//2
    else:
        print(req.text)
        break
    
