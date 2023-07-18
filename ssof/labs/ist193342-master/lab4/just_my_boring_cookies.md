# Challenge `Just my boring cookies` writeup

- Vulnerability: XSS vulnerability
- Where: *Search* bar
- Impact: We can inject any code in the *search* bar that will be reflected in the web browser

## Steps to reproduce

1. On the *Search* bar inject the following code: `<script>alert(document.cookie);</script>`
2. Click on *Search* and the cookies will be displayed on an alert box 
3. There is a cookie called **SECRET** whose value is the flag



