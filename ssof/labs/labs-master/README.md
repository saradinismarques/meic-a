# Labs of Software Security Course @ Técnico

Welcome to the Software Security Course @ Técnico!

Please read this page until the end before you start.

This repository is permanently under construction and its purpose is to provide you with tips for solving our challenges, as well as pointers for further study.

If you find something wrong or some topic that needs to be updated/added, please check [the issues page](https://gitlab.rnl.tecnico.ulisboa.pt/ssof2223/labs/-/issues) and create a new issue if necessary.

When you've read this page and are ready to begin, follow the links to the lab guides at the bottom.  
__The links that are marked (2021/22) have not yet been updated for the current semester (Fall 2022/23).__

The goal of these Software Security labs is for you to learn by doing, so you should strive to do your best.

In each lab you'll be challenged with 3 to 4 different vulnerability challenges associated with a given topic.  
In some cases after completing a challenge you'll find that the next challenge is very similar, but with the previous vulnerability fixed.  
In such cases there will always be some other vulnerability for you to find and exploit, but it may require a more powerful technique to exploit this time around!

Solving these challenges will be the basis for your lab evaluation, starting on Lab 2 (Week 2).

And now, an important piece of advice:

__Never run potential malicious content in your machine. You must install a VM (virtual machine) as a basic form of sandboxing.__

In this course we will strive to provide and refer you to software that is generally safe to use, but please use a VM to avoid potential damage to your system, accidental or otherwise.  
Ignore our warning at your own peril!

## 1. Virtual Machine

During these labs you will need a system with the right characteristics and the appropriate tools installed, and __we strongly recommend that you install a Virtual Machine for that__. You can pick your preferred distribution, or use one of the two options we provide below.

If you decide to use your OS of choice, please make sure that it is an x86_64 GNU/Linux distribution that's not too out of date and can build, run and debug 32 bit C programs.

### Option A. Debian VM

Our Debian VM can be downloaded here: [ssof_vm.2021-12-10.ova](https://drive.tecnico.ulisboa.pt/download/1695923672919286) (newest)

You can use these hashes to verify that you have the right file:

    SHA512 (ssof_vm.2021-12-10.ova) = c36ef519eaa1778627708e7f3badb0de3cbd3a3df3a7991189cf448a1cc70698df0287ca89c5516997c82675a5e1aad8972f3a9fa84cbc4afae1cf6a8676de7d
    SHA1 (ssof_vm.2021-12-10.ova) = 909b9e47c4eeae92041332cb37d3a5c8ded0dcd3

This VM is based on Debian GNU/Linux 11 amd64, with a KDE Plasma desktop environment.  
We hope that you'll find everything you need in it, but you can always install any additional software you require yourself.

More details about installing instructions, login details, list of installed software, and troubleshooting can be found [here](VM_debian.md).

### Option B. Ubuntu VM

Our Ubuntu VM can be downloaded here: [here](https://storage.ssof.rnl.tecnico.ulisboa.pt/).

You can use these hashes to verify that you have the right file:

    SHA1 (ubuntu_ssof.ova): 391a9de81f4c8a4f729a8380a9edddc340b8a8eb

This VM is a Ubuntu 18.04.1 VM and we hope you have in there everything you need for this course. It was created for the school year 2018/19 so the first thing to do after importing it is

    sudo apt update; sudo apt upgrade

More details about installing instructions, login details, list of installed software, and troubleshooting can be found [here](VM_ubuntu.md).

### Option C. None of the Above

If you are unable or unwilling to use your own computer, you can run our VM in the computers provided at the RNL and Tagus LTI Labs instead.  
If you have a computer that can run ssh and a VNC client, you can also use the RNL Lab computers remotely. Let us know if this is something you need.

## 2. Connect to Técnico VPN

In order to play these challenges and access the scoreboard you have to either:

- Connect to Técnico VPN, or
- Use an RNL Lab PC.

__It is not enough to be on the campus WiFi!__

When connecting to Técnico VPN, you can either:

- Connect inside of the VM
  - This way only traffic from the VM goes through the VPN
  - Our VM is already configured to do this easily. [See here](VM_debian.md#6-connecting-to-técnico-vpn-from-our-virtual-machine)
- Connect on your host system
  - This way *all* traffic on your computer goes through the VPN
  - [Instructions here.](https://si.tecnico.ulisboa.pt/servicos/redes-e-conetividade/vpn/) (Also applicable if you're using an alternative VM.)

__If you can't reach our servers, check your VPN connection! (And mistyped hostnames or port numbers!)__

## 3. Scoreboard

This year's labs we will have a [scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/) where you should submit the solutions for your challenges.

You'll need to register using an `@tecnico.ulisboa.pt` e-mail.  
The email needs to be of the form `your.name@tecnico.ulisboa.pt`, __NOT__ `istXXXXXX@tecnico.ulisboa.pt`, otherwise you won't receive the email to confirm your account!

If you don't have a suitable email address, please [contact us](mailto:pedro.adao@tecnico.ulisboa.pt?subject=[SSof]%20Scoreboard%20Registration%20Problem&cc=ana.matos@tecnico.ulisboa.pt).

And of course, __do not reuse an important password for your scoreboard account.__

## 4. Challenges

All challenges are hosted at `mustard.stt.rnl.tecnico.ulisboa.pt`. Each challenge runs on a specific port that will be given to you as part of the challenge.

Flags are secret strings of characters that you have to find and submit to the scoreboard to solve a challenge.  
__Unless the challenge description says otherwise,__ they are of the form: `SSof{....}`.  
For example: `SSof{This_is_an_example_flag}`.

Remember to copy the `SSof{}` part too, not just what's inside the curly braces!

These challenges will be used as the basis of your Lab evaluation (starting VSSD Lab 2 on Week 2), so do your best!

## 5. Links

- [Course Page](https://fenix.tecnico.ulisboa.pt/disciplinas/SSof/2021-2022/1-semestre/)
- [Scoreboard](https://scoreboard.ssof.rnl.tecnico.ulisboa.pt/)
- VMs
  - [Debian Virtual Machine Details](VM_debian.md)
  - [Ubuntu Virtual Machine Details](VM_ubuntu.md)
- [Lab 1 - Introduction](Introduction.md)
- [Lab 2 - Interacting with a Remote Server](Lab2-Interactions.md)
- [Lab 3 - Race Conditions](Lab3-RaceConditions.md)
- [Lab 4 - XSS](Lab4-XSS.md)
- [Lab 4 - CSRF](Lab4-CSRF.md)
- [Lab 5 - SQL Injection](Lab5-SQLi.md)
- [Lab 6 - Buffer Overflows](Lab6-BufferOverflows.md)
- [Lab 7 - Format Strings](Lab7-FormatStrings.md)
- [Extra - Buffer Overflows](Extra-BufferOverflows.md)
- [GDB](GDB.md)