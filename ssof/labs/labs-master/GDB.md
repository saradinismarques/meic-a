# GDB Basics

Below is a simple list of basic GDB commands. They should get you going for most of our exercises

- To analyse a program with gdb type `gdb <file_to_analyse>`
- To disassemble a function use:
 `disassemble <fn_name>` or `disassemble <memory_address>`
  - e.g. `disassemble main` or `disassemble 0x0804843b`.
  - in `gdp-peda` you can use `pdisass <fn_name/address>` to do it with colours.
- `b <memory_address>` inserts a breakpoint at address `memory_address`
  - eg `b *0x0804846a` or `b *main+47`
- `r` _runs_ the current program
- `c` _continues_ execution until the next breakpoint
- `n` executes the next instruction
- `s` steps into function `fn` when the instruction is a `call fn`
- `p` prints the value of an expression
  - `p variable_name` prints the content of the variable (if the symbol `variable_name` is defined)
  - `p &variable_name` prints the address where the variable is in memory
  - `p *memory_address` prints the content in this address
- `bt` prints a backtrace of the entire stack, that is, shows how you got to the current frame
- `info f` prints the information about the current frame. This is useful whenever you need to know where the return address of the function is stored and/or the value contained there.
- `stack n` shows the `n` registers of the stack after `esp`.
- `x/nx $rsp` --- shows the `n` registers after the register `$rsp`
- `x/nx address` --- shows the `n` registers after the address `address`
