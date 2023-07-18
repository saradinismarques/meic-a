# SQL Injection Lab (SQLi)

The goal for this lab is to learn the basics of SQLi attacks.

## What is SQLi

SQL Injection (SQLi) is a vulnerability that may exist in applications that access databases.
This vulnerability is present whenever the input provided by an attacker in not verified.
This may lead to situations where the input is included in query strings and as a consequence the attacker may perform queries in the database. This code is usually written in the form of small (partial) SQL sentences.

Although simple, this vulnerability is very powerful as an attacker may dump all the information in a database.

To demonstrate these attacks we will use a purposely ill-developed blog application hosted in our website.

Remember, __you should run these challenges inside a VM__ and __you must be in the IST VPN__ in order to be able to play these challenges.

## Problem 1

We will start with a simple problem of direct access to the database and will then move to more complex form of attacks.

### Task 1.1. Look at the website's functionality. Can you find a SQLi vulnerability? - Challenge `I will take care of this site`

Whenever looking for a SQLi we should first find the fields that are injectable.

- Can you find them?
- Ok, can you now login as the `admin` and read his profile? Look for vulnerabilities in the login form.
- Submit the flag in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Task 1.2. And why not become rich? - Challenge `Money, money, money!`

(Note: unlocked after completing `I will take care of this site`)

Create your own user. __DO NOT USE HERE A MEANINGFUL PASSWORD! THIS SITE IS COMPLETELY BROKEN!!!!__

We heard that there is a lottery going on that might make you rich. Do you want to be rich? Get the JACKPOT! It is a different one for every player.

- But how come as your tokens are _readonly_?... It would be so much easier if we could just get more _tokens_...
- Oh, and by the way we know that you usually comment out the rest of the lines with `--` or `/*` to bypass some checks. Don't try it here. We are covered on this.
- Submit the flag in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Task 1.3. And now for some really cool stuff - Challenge `Wow, it can't be more juicy than this!`

(Note: unlocked after completing `Money, money, money!`)

Are there any other interesting information in this website? We have heard that there is a juicy secret blogpost yet to be released. Can you find it?

- Are there any other vulnerable input fields? Look for a place where you haven't tried to inject into yet.
- Oh, and it might be useful to have a look at `sqlite_master`. Someone mentioned `tbl_name` and `sql` but we have no clue of what this is.
- Submit the flag in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

## Problem 2

### Task 2.1. - Challenge `Sometimes we are just temporarily blind`

(Note: unlocked after completing `Wow, it can't be more juicy than this!`)

The admin was in a hurry but he managed to fix the login and update profile problems! He just lacked the time to fix the search bar injection... but to prevent it from being exploited the `admin` just stopped showing the blog posts.

- Can you still exploit it?
- Is there any other information that can be extracted from the database?
- `requests` package for Python might be useful for this challenge as you might need to do some scripting. Look at an example below. You can also find [here](./code/requests_template.py) a template on how to use module `requests`.
- Submit the flag in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

```python
import requests

SERVER = f'http://{server}:{port}/'

#### GET REQUESTS
params = {'search' : 'lorem'}
headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}

r = requests.get(SERVER, params=params, headers=headers)

#### ANSWERS
print(f'status     : {r.status_code}')
print(f'headers    : {r.headers}')
print(f'cookies    : {r.cookies}')
print(f'html       : {r.text}')
```

## Conclusion

In this lab you learned that in the presence of a SQL injection vulnerability it is possible to perform queries and execute actions other than the ones expected by the application.

## Assessment

__Important:__ Given that Saturday is Christmas Eve, the __deadline for this week's exercises is postponed to Wednesday, December 28, 5pm__.

This week the exercises used for assessment are:

- I will take care of this site (5 points)
- Money, money, money! (5 points)
- Wow, it can't be more juicy than this! (5 points)
- Sometimes we are just temporarily blind (5 points)

You should submit a writeup on how you solved the challenges. For that, create a folder named `lab5` in the repo assigned to you, and create __one writeup per challenge__ named `name_of_the_challenge.md`.
A sample can be found [here](writeup.md).
