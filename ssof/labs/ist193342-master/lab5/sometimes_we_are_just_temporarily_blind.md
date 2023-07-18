# Challenge `Sometimes we are just temporarily blind` writeup

- Vulnerability: Boolean SQL injection
- Where: *Search* bar
- Impact: We can inject SQL code in the *Search* bar that will be executed

## Steps to reproduce

1. General idea: Since it's a boolean SQL injection like the hint says, do a brute force attack by changing the various payloads of **SELECT** operations to extract the information we want. By doing this payloads and having returned something like "Found 1 article..." we know that what we wrote is true so what we selected exists. On the opposite if we get "Found 0 articles..." we know that what we selected doesn't exist
2. First let's look for the hidden table name present on the database as the hint suggests. On a python script in a loop we try injecting the payload `my search' UNION SELECT 'a', sql, name FROM sqlite_master WHERE type ='table' AND name LIKE '%'+word[:-1]+'%' --` where the *word* is one of the words in the list we provided in a .txt file. Running the program we get the words 'super' and 'secrets' and by trying different payloads we conclude the name of the table is something like `super_%_secrets` where % is something we haven't found yet ([1] on the script)
3. Next we look for the lenght of the % part with the same logic and we get 5 ([2] on the script)
4. Next we want to find the remaining 5 characters that are in the % part. Again with the same logic and by running the script we get 's', 'o', 'f' and '_'. By trying different payloads knowing this new information we get the name of table which is `super_s_sof_secrets` ([3] on the script)
5. The next step is finding the columns names on this table. Doing the same as in step 2. but with the payload `my search' UNION SELECT '+ word[:-1] + ', 'a', 'b' FROM super_s_sof_secrets --` we get the names `id` and `secret` so we assume the flag is on the column `secret` ([4] on the script) 
6. The next step is finding words present on a post in this table in this column with a content similar to 'SSof{%}' that is the flag format. We use the same logic as in step 2. again but with the payload `my search' UNION SELECT id, secret, 'a' FROM super_s_sof_secrets WHERE secret LIKE '%SSof{%' + word[:-1] + '%}%' --`. We get the words 'am', 'blind', 'boolean', 'can', 'data', 'get', 'injection', 'only', 'partially', 'since', 'using', 'your' ([5] on the script)
7. Next we find the size of the flag by doing a payload similar to step 3. and we get 75 ([6] on the script)
8. Next we find the order of the words on the flag starting with one word and completing what's before and after it by running the script multiple times and we get `SSof{%_am_only_partially_blind_since_%_can_get_your_data_using_boolean_injection}`. Knowing the flag size and with logic we get `SSof{i_am_only_partially_blind_since_i_can_get_your_data_using_boolean_injection}` ([7] on the script)
9. If we try to submit the flag like this we get *Incorrect Answer* so some letters must be capitalized. We test each letter by sending two payloads in upper and lower cases and check which one is right. This time we use **GLOB** instead of **LIKE** because it's case sensitive. Finally we get the flag SSof{I_am_only_partially_blind_since_I_can_gEt_yoUr_datA_using_Boolean_Injection} ([8] on the script)

This was done with the python script [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab5/sometimes_we_are_just_temporarily_blind.py) and the list of words used for the dictionary attack [here](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab5/word_list.txt)

