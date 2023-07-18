# VM

__Never run potential malicious content in your machine. You must install a VM as a basic form of sandboxing.__

In order to do the challenges for this course you must have a Virtual Machine with the appropriate tools installed. You can pick your preferred distribution, or use the one we provide you [here](https://storage.ssof.rnl.tecnico.ulisboa.pt/).

    SHA1SUM (ubuntu_ssof.ova): 391a9de81f4c8a4f729a8380a9edddc340b8a8eb

`ubuntu_ssof.ova (4GB)` is a Ubuntu 18.04.1 VM and we hope you have everything you need for this course in there. It was created for the school year 2018/19 so the first thing to do after importing it is

    sudo apt update; sudo apt upgrade

## 1. Importing a VM to Virtual Box or VMware Fusion to your machine

- How [to import an existing VM into VirtualBox](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html)
- How [to import an existing VM into VMware Fusion](https://pubs.vmware.com/fusion-5/index.jsp?topic=%2Fcom.vmware.fusion.help.doc%2FGUID-275EF202-CF74-43BF-A9E9-351488E16030.html)

If using VirtualBox do not forget to install Guest Additions in order to have higher screen resolution and allowing copy host-to-guest.

## 2. Login details for the VM

__Do not forget to change this passwd!__

    user: Ssof
    passwd: ssof

## 3. Installed Tools

### Web

- firefox
- chrome
- curl
- python module 'requests'
- burp suite community edition
- OWASP ZAP (an open source alternative to Burp Suite)

### Reverse and pwn

- IDA freeware
- radare2
- Cutter (radare2 GUI)
- gdb
- pwndbg (gdb plugin)
- python module `pwntools`
- ROPGadget

### Other

- vim
- vscode
- git
- python
- python-pip

## 4. Running a VM using `rnl-virt` in RNL (labs in Alameda)

__@ToDo__

## 5. Running a VM in labs in Tagus

__@ToDo__

## 6. Troubleshooting

### `gdb` stops working after update

If this happens, the workaround is to revert `gdb` to an earlier version. Details [here](https://bugs.launchpad.net/ubuntu/+source/gdb/+bug/1845494).

```bash
sudo apt purge gdb
sudo apt install gdb=8.1-0ubuntu3
echo "gdb hold" | sudo dpkg --set-selections
```

### Screen resolution problems when using Virtual Box

If you have problems with the Guest Additions (screen resolution, unable to copy host to guest, etc) you might want to have a look in [here](http://www.virtualbox.org/manual/ch04.html#idp11569008).

### Problems installing `pwntools`

If you have problems installing `pwntools` with `pip3` just update `pip3`

      sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall

### Problems with MacOS Catalina and VirtualBox 6.1.14

It has been reported crashes when using VirtualBox 6.1.14 and MacOS Catalina [here](https://forums.virtualbox.org/viewtopic.php?f=8&t=99762). Proposed solution is rollback to VirtualBox 6.1.12.
