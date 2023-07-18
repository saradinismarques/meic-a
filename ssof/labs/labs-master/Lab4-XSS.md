# Cross-Site Scripting Lab (XSS)

The goal for this lab is to learn the basics of XSS attacks.

## What is XSS

Cross-site scripting (XSS) is a vulnerability that may exist in web applications.
This vulnerability is present whenever an attacker is able to inject malicious code in a webpage. This code is usually written in the form of a small JavaScript program and will be run by the web browser of the client that accesses that webpage. This code may be included in the client's request or already present in the website. These two types of XSS are called respectively _Reflected XSS_ and _Stored XSS_.

Although simple, this vulnerability is very powerful as an attacker may steal the victim’s credentials, such as cookies, allowing him to impersonate the victim.

To demonstrate these attacks we will use a purposely ill-developed blog application hosted in our website.

Remember, __you should run these challenges inside a VM__ and __you must be in the IST VPN__ in order to be able to play these challenges.

## Problem 1

This problem is running at: see challenge _Just my boring cookies_ in the scoreboard.

We will start with a simple problem of using malicious code against ourselves and will then evolve to a scenario where we will use malicious code against the `admin` of our platform.

### Task 1.1. Look at the website's functionality

_Can you find a XSS vulnerability?_

The first task whenever you are looking for a XSS vulnerability is to do some recon of the system searching for the presence of the vulnerability. Can you find one? Can you find a place where you can inject code that will be _reflected_, i.e., executed in your own browser?

Try to inject that code and see what happens.

- Does it affect just yourself? Or everyone else?

### Task 1.2. Find a way to display your own cookies on the screen - Challenge `Just my boring cookies`

Ok, you were able to find a place where you can inject code but can you make it more interesting? Can you use it to steal your own cookies and display them on the screen?

- Get your first flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Task 1.3. Send your cookies to a website you control

At this point you know how to display your own cookies in your screen but can you send them to a website that you control?

To have a website you control, you have 2 options:

1. Use an online service to collect your http requests such as [Webhook](https://webhook.site/) or [RequestBin](https://requestbin.com/). Both these services work the same way: you are provided with a unique URL to where you can make requests and observe the content of such requests

    - To connect to your bin just use `https://webhook.site/<random_identifier_you_were_given>`.
    - Upon refreshing the page, you have there all the connections established with your bin.

2. Host it in a machine in Técnico

    - you may use your Técnico's credentials to SSH to `nexus.rnl.tecnico.ulisboa.pt` (e.g. `ssh <your_ist_user>@nexus.rnl.tecnico.ulisboa.pt`) and run `nc -vv -l -p PORT` to listen for a request on `PORT` (use a PORT between 30000 and 40000) and use `ip a` to get the `IP` address of the machine. `IP` of `nexus` should in principle be `193.136.164.129`.
    - _Do not forget that `nc -l` is only able to establish a single connection. Once you establish it, you have to re-run `nc -vv -l -p PORT` to listen to a new one._
    - You can then test if it is indeed listening by going to the browser and running `http://IP:PORT` and see if you get anything in `nexus`.

3. Host it in `sigma`

    - You may use `sigma.tecnico.ulisboa.pt` however in this case there is some load balancing involved and your `ip` address will possibly be different every time you login. Remember to check it with `ip a` after you login!

Once this is set up, were you able to get your cookies in the website you control (e.g., `nexus`)?

- Have a look at `window.location`. It might be useful.
- _In some cases you might need to encode `+` as `%2B`_.
  
### Task 1.4. Steal admin's cookies - Challenge `My favourite cookies`

Can you find a way to steal the cookies of the `admin` of our website? As you have seen, there is a cookie `SECRET` in our application. You found yours in Task 1.2. The admin's cookie is different, after all he is the admin.

The goal here is to _lure_ the admin to perform a request to the site where you are collecting the cookies. If he does that, then his request will have his cookies and consequently you will learn his `SECRET`.

- You can use the XSS payload developed at Task 1.3.
- First, can you lure one of your colleagues and steal his cookie? Team up in groups of two for this task.
- Now, how can you _lure_ the admin to click the link with the vulnerability you found?
  - _Hint: The admin is very curious about your bug/feature request_.
- Get your second flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Lessons Learned

Although we have used this technique against ourselves, you can easily see that it is possible to _lure_ someone else into clicking in a link that will run code in his own browser (as you did in Task 1.4).

## Problem 2

(Note: unlocked after completing `My favourite cookies`)

### Task2.1. Bypassing simple WAF - Challenge `Give me more than a simple WAF`

Now it seems like the developers created a very simple WAF that is blocking some words like `script` and `img`, and the traditional bypasses `sCript`, `SCriPT`, etc.

- What happens when you try your old scripts? Are you blocked?
- Find another way to get the `admin`'s cookie.
- Get another flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Lessons Learned

Avoid using _ad-hoc_ filtering techniques. Rely on standard sanitization techniques.

## Problem 3

(Note: unlocked after completing `My favourite cookies`)

This problem is running at: see challenge _Go on and censor my posts_ in the scoreboard.

It seems that this feedback form is giving us enough problems so we decided to disable it.
Also, we figured out that we would need more than a clumsy WAF and this time we asked our developers to properly protect ourselves from XSS attacks by properly escaping the necessary characters.

### Task 3.1. Analyse escaped solution

Try your old attacks in this new version. View the page-source after running your attack and check the differences (comparing with Problem 1). Check also the different answers.

### Task 3.2. Explore the new feature. Review blogposts - Challenge `Go on and censor my posts`

Now our application allows you to submit new blogposts but, in order to perform a triage of malicious content, we have to review it first before putting it online. But no worries, we are using the most recent AI+blockchain technology and we do it really fast. Five seconds max!

In fact, to avoid chaos, your blogposts will be reviewed but will never be shown in the main page nor in search. After solving the challenge, you will agree with us :-)

- Explore the new feature. Can you find any bugs in it?
- Don't just try a default payload. Use `view-source` to see what is actually happening in the html.
- __Bear in mind that the `admin` WILL ONLY REVIEW YOUR POST once you click `Update post and send it for admin review`__.
- Do you know what the `XMLHttpRequest` JavaScript object does?
- Recall that `nc` can only handle a connection at a time. You better use [Webhook](https://webhook.site/) this time.
- Get another flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Task 3.3. Content Security Policy - Challenge `Read my lips: No more scripts!`

(Note: unlocked after completing `Go on and censor my posts`)

We just learned about [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) and from now on we do not allow inline scripts. We are completely safe now. Are we?

- Try your solution from Task 3.2. Does it work?
- Do you know what went wrong? Looking at the logs in the Console of the browser might give you some hints.
- Are we really preventing all scripts from running? Analyse Content Security Policy directive: `script-src *`.
- Get another flag and submit it in our [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/).

### Lessons Learned

1. There are more to XSS than reflection attacks.
2. You do not need to include all your code in the payload. It may be called from somewhere else this way obfuscating its malicious intent.

## Conclusion

In this lab you learned that it is possible to execute malicious code in a victim's browser and in particular to steal the victim's credentials by performing XSS attacks. We did not illustrate what you could do with these credentials but, as it is expected, you can do mostly everything that a user could do with such cookies. If these credentials were the session credentials of the user then you could perform the same actions as the user.

## Assessment

This week the exercises used for assessment are:

- Just my boring cookies (4 points)
- My favourite cookies (4 points)
- Give me more than a simple WAF (4 points)
- Go on and censor my posts (4 points)
- Read my lips: No more scripts! (4 points)

You should submit a writeup on how you solved the challenges. For that, create a folder named `lab4` in the repo assigned to you, and create __one writeup per challenge__ named `name_of_the_challenge.md`.
A sample can be found [here](writeup.md).
