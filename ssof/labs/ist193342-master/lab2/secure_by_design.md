# Challenge `Secure by Design` writeup

- Vulnerability: Cookies can be changed in the web browser itself 
- Impact: By accessing the website as *admin* we get the flag
  
## Steps to reproduce

1. Enter the page that appears after entering your nickname by writing a random name on the form
2. On the next page where they check if the user is *admin* do a righ-click and inspect the page
3. In the tab **Storage** and in the section **Cookies** there is a cookie **user** and its value is what we wrote previously but encoded in base64
4. Double click on the value and we can edit it to *admin* but encoded in base64 *YWRtaW4=*

This was done directly in the web browser and no script was necessary.
