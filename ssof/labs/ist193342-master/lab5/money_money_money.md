# Challenge `Money, money, money!` writeup

- Vulnerability: SQL injection
- Where: *Bio* section
- Impact: We can inject SQL code in the *Bio* section that will be executed

## Steps to reproduce

1. This time commenting out some lines to bypass some checks doesn't work so register a new user and login with it
2. On the *Profile* section check the number of tokens you need to win the jackpot (e.g. 31309) 
3. On the *Bio* inject the following code: `', tokens='31309`
4. Click on *Update profile* and the number of tokens will be updated to the value we choose. In the end of the page there will be the flag

