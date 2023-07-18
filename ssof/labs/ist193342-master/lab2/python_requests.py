import requests
import re

while(True):
    
    s = requests.Session()
    req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22053')
    target = int(re.findall(r'[0-9]+', req.text)[0])
    print('Target: ' + str(target))

    finished = False

    while(True):
        req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/more')
        total = int(re.findall(r'[0-9]+', req.text)[2])
        print('Total: ' + str(total))

        if(total > target):
            break
        elif(total == target):
            print(s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/finish').text)
            finished = True
            break
        else:
            continue
            
    if(finished):
        break    
