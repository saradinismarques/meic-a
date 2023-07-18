# Cross-Site Request Forgery Lab (CSRF)

The goal for this lab is to learn the basics of CSRF attacks.

## What is CSRF

Cross-site request forgery (CSRF) is a vulnerability that may exist in web applications and that allow a malicious user to perform actions in a site where the victim has an active session.

These attacks involve 3 parts:

* A _vulnerable_ trusted site (`T`)
* A victim (`V`) that has an active session in `T` (for the sake of simplicity let's say that the victim is logged in in `T`)
* A malicious site (`M`) controlled by the attacker that contains malicious code.

The attack is simple. Suppose that the trusted site `T` is vulnerable to CSRF attacks, and that `V` is logged in in `T`. If the victim visits a malicious website `M` containing malicious code, then this malicious code will run in `V`'s web browser and will perform an action in `T` (on behalf of `V`). As in the case of `XSS` this code is usually written in the form of a small JavaScript program.

Although simple, this vulnerability is very powerful as an attacker may perform actions in a legitimate site using the credentials of the victim.

To demonstrate these attacks we will use our purposely ill-developed blog application.

Remember, __you must be in the IST VPN__ in order to be able to play these challenges.

## Problem 1 - Challenge `You just Became Older`

### Task 1.1. Understand CSRF and perform a simple Proof of Concept (POC)

Start by teaming up in groups of two for this task (one will play the `victim (V)` and the other will play the `attacker (A)`) and understand the concepts behind Cross Site Request Forgery (CSRF).

* Look at the new website. CSRF requires the existence of an authenticated session. Is there any _insecure_ authentication mechanism?
* Exploit it! You will need some _basic cooperation_ from `V`.

    1. `V` logs into our trusted (but insecure) blog website.
    2. `A` creates a malicious website `M` that will exploit this vulnerability.
    3. `A` should now _lure_ `V` into going to `M`.
        * This will perform an action in `V`'s account without him noticing.
    4. Did something changed in `V`'s account?
    5. There is no flag for this task.

* Tips:
  * for `A`: You may want to use Burp Suite or OWASP ZAP to look at how the authenticated requests are being made. In particular, look at the `update_profile` operation.
  * for `A`: You may use your `sigma` account for this. Create a folder `ssof` under the folder `web` and create there your malicious site. It can be a simple php webpage.

### Task 1.2. Identify possible counter-measures

* Why are CSRF attacks possible?
* What counter measures could be put in place to protect `T` from CSRF attacks?
* What is a CSRF token?

## Conclusion

In this lab you learned that it is possible to execute unintended actions in a web site where a victim is logged in, if that website is vulnerable to CSRF attacks. You also learned that it is possible to prevent these attacks with the addition of tokens other than cookies.
