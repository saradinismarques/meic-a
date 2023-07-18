# Buffer Overflow Exploitation (Extra class)

These challenges are extra class and are here for those willing to learn more about buffer overflows.

## Task 2 -- Exercises with Active Protection (Extra class)

### 1. Canaries (Extra class)

Canaries are in place to protect us and prevent buffer overflows. Really?

File `01_canary_basic.c` was compiled with canaries and does not allow execution in the stack (XP enabled).

This challenge is running at: see challenge _Canaries_ in the scoreboard.

### 2. More Canaries (Extra class)

Oh _Canaries_ was just to easy. Now we will not leak the canary for you. Good luck!

File `02_canary_leak.c` was compiled with canaries and does not allow execution in the stack (XP enabled).

This challenge is running at: see challenge _More Canaries_ in the scoreboard.

### 3. Simple Leak (Extra class)

Now everything changes in each run given that ASLR is enabled. The stack and the code are always in a different place. Can you still win the game? (with some help from our friends...)

To run this challenge locally on your computer you need to __enable__ ALSR.

File `01_aslr_leak.c` was compiled with no-canaries but does not allow execution in the stack (XP enabled).

This challenge is running at: see challenge _Simple Leak_ in the scoreboard.

### 4. Simple Leak++ (Extra class. This one is tough!)

Follow-up of _3. Simple Leak_. Our friends provided you to much help leaking the address of the function. Can you do it on your own? Everything is changing again in each run given that ASLR is enabled.

To run this challenge locally on your computer you need to __enable__ ALSR.

File `02_aslr2_leak.c` was compiled with no-canaries but does not allow execution in the stack (XP enabled).

This challenge is running at: see challenge _Simple Leak++_ in the scoreboard.

_Tip:_ You can use `pwntools` instruction `elf.symbols['fn']` to get the address of function `fn` in binary `bin` and `next(elf.search(string))` for the address of the occurrence of `string` in the binary.

    from pwn import *

    context.arch = 'i386'
    context.os = 'linux'

    elf = ELF('./bin')
    addr_fn = elf.symbols['fn']
    addr_string = next(elf.search(string))

### 5. Welcome to your first ret2libc (Extra class. This one is even tougher!)

Enough. Now you can no longer execute code in the stack. Can you still call `/bin/sh`?

_Do not forget to disable ALSR again._

File `01_retlibc.c` was compiled with no-canaries and `-no-pie` but does not allow execution in the stack (XP enabled).

This challenge is running at: see challenge _Welcome to your first ret2libc_ in the scoreboard.

_Tip:_ It might be worth reading [this](https://www.shellblade.net/docs/ret2libc.pdf), in particular how the stack frame has to be constructed (middle page 7-top page 11).

### 6. ROP (Extra class. This one is 31337!)

Follow-up of _5. Welcome to your first ret2libc_. Calling `system` was just to simple so we removed it from our `bin`. Can you still do it without `system`?

_Do not forget to disable ALSR again._

_Tip:_ Have you heard of `ROPGadget`? It might be useful to generate the ROP-chain for this challenge.

File `05_rop_get_shell` was compiled with no-canaries and `-no-pie` but does not allow execution in the stack (XP enabled).

This challenge is running at: see challenge _ROP_ in the scoreboard.
