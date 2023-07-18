# Format Strings Vulnerability Lab

The goal of this lab is to analyse and exploit format-strings vulnerabilities.  
For this lab we propose a series of simple format string exercises that range from reading values that are stored in the local stack (`Simple Local Read`) to changing the return address of a function (`Call Function Again`).

Format String Vulnerabilities exist whenever a `printf(str)` is improperly used and the format string `str` is controlled by the adversary. This allows reading arbitrary memory content, write to arbitrary memory content, and hijack of the execution control flow.

To interact with the server you can adapt the following snippet: [netcat_template.py](code/netcat_template.py)

## Setup

- Notice that these files do not need to be compiled with `-fno-stack-protector` nor `-z execstack` but you need to disable the ASLR for all of them (this is global for the OS)

```bash
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

- The information on how each file was compiled is at the header of each source file.
- Do not know how to use GDB? A quick GDB-101 with a list of basic GDB commands can be found [here](GDB.md)

## Task 1 - Reading Arbitrary Values from Memory

### 0. Simple Local Read

Let us start with exercise `00_local_read.c`. The goal of this exercise is to read the variable `secret_value`. How can you do it?

1. Recall how you can read the entire stack with `printf` (in the presence of a format string vulnerability).
2. Where is `secret_value` located?

This challenge is running at: see challenge _Simple Local Read_ in the scoreboard.

#### Tips

- Whenever in the presence of a format string vulnerability, the first thing we do is to try to understand the stack. The idea is to ask for several `%x` for which we did not push the corresponding arguments to the stack. For example, send `AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x`. What will this do?
  - This will print the string `AAAA` followed by 20 other hex values (one for each `%x`) that correspond to the content of the 20 registers of the stack immediately after the format string of the `printf`.
    - To improve readability we used `%08x` to print the values in hex and padded with `0`'s to the left to use 8 characters.
    - To improve readability we also used `.` to separate the printed registers.
- Since you know that the string `secret_value` was loaded into the stack, it means that the address where `secret_value` is located is in the stack and so, using `%s` instead of `%x` allows one to read the value pointed by such address.
- Be careful when using `%s` on an address that is `NULL`.
  - What can go wrong?

### 1. Short Local Read

Now we have a much smaller buffer to write into. Can we still do it?

#### Tips

- Recall that you can use positional arguments `%N$t` with `printf` (where `N` is a number and `t` is a format specifier). This allows printing the `N`-th register of the stack immediately after the format string without the need to print the previous `N-1`.
- Where is `secret_value` located?

This challenge is running at: see challenge _Short Local Read_ in the scoreboard.

## Task 2 - Writing Values to Memory

### 2. Write to Memory

Function `printf` also allows you to write on variables using the format string `%n`.

- Can you change the value of `target` to a value other than `0`?
- Notice that target is not in the stack.

This challenge is running at: see challenge _Write to Memory_ in the scoreboard.

#### Tips

- Like `%s` allows one to read the value pointed by an address in memory, `%n` allows one to write a value to an address in memory.
  - What does `%n` writes to that address? It writes the number of characters printed so far.
- The first thing to do again is to inspect the stack by sending an arbitrary number of `%x`.
- Do you see `41414141`? What does it mean? `41414141` is the `AAAA` that we have introduced at the beginning of our string. This means that the 7th register on the stack is the beginning of `buffer` and is controlled by us.
- How can you write into `target`?
  - Do you know its address? Remember that `target` is a global variable and you have the binary that is running on the server.

    ```python
    from pwn import *

    elf = ELF(PROG_NAME)
    target_address = elf.symbols['target']
    ```

  - What happens if instead of `AAAA` you write the address of `target` at the beginning of our string?
  - And if your 7th `%` is a `%n` instead of `%08x`?

### 3. Write Specific Value

And can you change the value of `target` to a specific value?

This challenge is running at: see challenge _Write Specific Value_ in the scoreboard.

#### Tips

- Recall that you can always print as many characters as you want (up to a reasonable amount). Either explicitly, eg `AAAAAAAAAAAAAAAAAAAA`, or using padding `%20x`.

### 4. Write Specific Byte

And can you write a specific value in `target`? One whose _most significant byte_ is not `0`?

This challenge is running at: see challenge _Write Specific Byte_ in the scoreboard.

#### Tips

- Do not forget that you can apply modifiers to format strings, eg `%hhn`, to write a single byte.
- Also remember that the most significant byte of memory address `0x08041010` is byte `0x08041013`.

### 5. Write Big Numbers

Well, but you cannot do it if you have to write a very big number. Or can you?

This challenge is running at: see challenge _Write Big Numbers_ in the scoreboard.

#### Tips

- Do not forget the modifiers `hh` (1 byte) and `h` (2 bytes).

### 6. Write Given Number

Enough! Now I tell you what to write. Can you do it?

This challenge is running at: see challenge _Write Given Number_ in the scoreboard.

## Task 3 - Call Functions

### 7. Calling Functions

Let's see if you can now call functions. Can you call function `win`?

- Notice that function `exit` is being called...
- You might need to use `objdump -R bin` to know the address of `exit@GOT`.
  - Have you haver heard of GOT?

Alternatively

```python
from pwn import *

elf = ELF(PROG_NAME)
win_address = elf.symbols['win']
exit_address = elf.got['exit']
```

This challenge is running at: see challenge _Calling Functions_ in the scoreboard.

### 8. Call Function Again

I will not call `win` for you anymore. Can you do it by yourself?

This challenge is running at: see challenge _Call Functions_ in the scoreboard.

## Summary

The steps to perform a Format String Attack are thus the following:

1. Send `AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x` to read the content of the 20 registers of the stack immediately after the format string of the `printf`.
2. Is the value in the stack? __Yes__, and suppose that it is the 5th register below the format string.
    - is it an integer? Then send `%08x.%08x.%08x.%08x.%d` (or alternatively `%5$d`).
    - is it a string (so you have a pointer to it in the 5th position)? Then send `%08x.%08x.%08x.%08x.%s` (or alternatively `%5$s`).
    - is it a pointer to an address where you want to write? Then send `%08x.%08x.%08x.%08x.%n` (or alternatively `%5$n`). This will write 36 in that address (the alternative solution writes `0`).
3. Is the value in the stack? __NO__, but suppose that `41414141` appears in the 10th position after the format string. In this case you just have to add the address to the stack.
    - If the address you want to read is `0x08042010`, then send `\x10\x20\x04\x08.%10$s` to read the content of this address.
    - If the address you want to write is `0x08042010`, then send `\x10\x20\x04\x08.%10$n` to write `5` into this address (one for each of the bytes, plus one for the dot `.`).
4. How do you write arbitrary values? Use `%Nx` to adjust the number of characters that are printed. In this case `N`.
    - Be careful that the number of printed characters does not reset after a `%n`.
    - The way to write `8` and then `4` is to print `252` extra characters as `(8+252) % 256 = 4`.
    - Also, you might want to use `%hhn` to write a single byte and not damaging the _bytes to the left_.

---

## Assessment

This week the exercises used for assessment are:

- Simple Local Read (2.5 points)
- Short Local Read (2.5 points)
- Write to Memory (2.5 points)
- Write Specific Value (2.5 points)
- Write Specific Byte (2.5 points)
- Write Big Numbers (2.5 points)
- Write Given Number (2.5 points)
- Calling Functions (1.25 points)
- Call Function Again (1.25 points)

You should submit a writeup on how you solved the challenges. For that, create a folder named `lab7` in the repo assigned to you, and create __one writeup per challenge__ named `name_of_the_challenge.md`.
A sample can be found [here](writeup.md).
