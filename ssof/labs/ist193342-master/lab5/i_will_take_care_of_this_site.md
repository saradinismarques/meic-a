# Challenge `I will take care of this site` writeup

- Vulnerability: SQL injection
- Where: *Login* form
- Impact: We can inject SQL code in the *Login* form that will be executed

## Steps to reproduce

1. On the *Login* form inject the following code on the username: `' or 1=1 --` and write anything for the password. This will cause the query to be `SELECT * FROM users WHERE username = '' OR 1=1 -- ' AND password = 'foo'` which is the same as `SELECT * FROM users WHERE username = '' OR 1=1`. This way we will be logged in as **admin**
2. After logged in click on the *Profile* section and on the *Bio* there is the flag

